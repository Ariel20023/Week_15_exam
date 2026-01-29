from fastapi import FastAPI
from db_init import init_database
from dal import *
from db import *
app = FastAPI()

init_database()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/q1/customers-credit-limit-outliers")
def customers_credit_limit_outliers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_customers_by_credit_limit_range())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

@app.get("/q2/orders-null-comments")
def orders_null_comments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_orders_with_null_comments())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


@app.get("/q3/customers-first-5")
def customers_first_5():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_first_5_customers())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


@app.get("/q4/payments-total-average")
def payments_total_average():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_payments_total_and_average())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


@app.get("/q5/employees-office-phone")
def employees_office_phone():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_employees_with_office_phone())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


@app.get("/q6/customers-shipping-dates")
def customers_shipping_dates():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_customers_with_shipping_dates())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


@app.get("/q7/customer-quantity-per-order")
def customer_quantity_per_order():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_customer_quantity_per_order())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows


@app.get("/q8/customers-payments-by-lastname-pattern")
def customers_payments_by_lastname_pattern():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(get_customers_payments_by_lastname_pattern())
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

