from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import numpy as np
from pydantic import ValidationError

from db import get_connection, init_db
from models import Weapon

app = FastAPI(title="Weapon API")

@app.on_event("startup")
def startup():
    init_db()

@app.post("/upload")
def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV allowed")

    try:
        df = pd.read_csv(file.file)
        df['manufacturer'] = df['manufacturer'].replace({np.nan: None})
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid CSV file")

    if df.empty:
        raise HTTPException(status_code=400, detail="CSV is empty")

    # validation
    for i, row in enumerate(df.to_dict("records"), start=1):
        try:
            Weapon(**row)
        except ValidationError as e:
            raise HTTPException(status_code=422, detail={"row": i, "error": e.errors()})

    # pandas processing
    df["manufacturer"] = df["manufacturer"].fillna("Unknown")

    bins = [-1, 20, 100, 300, float("inf")]
    labels = ["low", "medium", "high", "extreme"]
    df["level_risk"] = pd.cut(df["range_km"], bins=bins, labels=labels)

    conn = get_connection()
    cursor = conn.cursor()

    insert_sql = """
        INSERT INTO weapon (
            weapon_id, weapon_name, weapon_type,
            range_km, weight_kg, manufacturer,
            origin_country, storage_location,
            year_estimated, level_risk
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = [
        (
            r.weapon_id, r.weapon_name, r.weapon_type,
            r.range_km, r.weight_kg, r.manufacturer,
            r.origin_country, r.storage_location,
            r.year_estimated, df.loc[i, "level_risk"]
        )
        for i, r in enumerate(df.itertuples(index=False))
    ]

    cursor.executemany(insert_sql, values)
    conn.commit()

    cursor.close()
    conn.close()

    return {
        "status": "success",
        "inserted_records": len(values)
    }
