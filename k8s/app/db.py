import os
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "weapon")
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weapon (
        id INT AUTO_INCREMENT PRIMARY KEY,
        weapon_id VARCHAR(20),
        weapon_name VARCHAR(50),
        weapon_type VARCHAR(50),
        range_km INT,
        weight_kg FLOAT,
        manufacturer VARCHAR(50),
        origin_country VARCHAR(50),
        storage_location VARCHAR(50),
        year_estimated INT,
        level_risk VARCHAR(20)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
