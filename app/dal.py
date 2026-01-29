from typing import List, Dict, Any

def get_customers_by_credit_limit_range():
    return """select customerName  , creditLimit 
                from customers
                 where creditLimit < 10000
                  or creditLimit > 100000;"""

def get_orders_with_null_comments():
    return """select orderNumber , comments text
            from orders
            where comments text IS NOT NULL
            ORDER BY orderDate ;"""

def get_first_5_customers():
    return """SELECT customerName,contactLastName,contactFirstName
            FROM customers
            order by contactLastName
            LIMIT 5;"""

def get_payments_total_and_average():
    return """select SUM(amount) AS lump_sum ,MIN(amount) AS minimum_amount ,MAX(amount) AS max_amount ,AVG(amount) AS avg_amount
	        FROM payments; """

def get_employees_with_office_phone():
    return """SELECT e.firstName , e.lastName , o.phone
            FROM employees AS e
            left JOIN offices AS o
            on e.officeCode = o.officeCode; """

def get_customers_with_shipping_dates():
    return """SELECT customerName ,o.orderDate
            FROM customers as c
            LEFT JOIN orders as o
            on c.customerNumber = o.customerNumber;"""


def get_customer_quantity_per_order():
    return """SELECT c.customerName ,o.quantityOrdered
            from customers as c
            LEFT JOIN orders as ord
            ON c.customerNumber = ord.customerNumber
            LEFT JOIN orderdetails as o
            ON ord.orderNumber = o.orderNumber
            GROUP BY c.customerName;"""


def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    return """SELECT c.customerName ,e.firstName, SUM(p.amount) as sum_amount
            from customers as c
            LEFT JOIN employees as e
            on c.salesRepEmployeeNumber = e.employeeNumber
            LEFT JOIN payments as p
            on p.customerNumber = c.customerNumber
            where e.firstName LIKE "%Mu%" or e.firstName like "%ly%"
            GROUP by  c.customerName ,e.firstName
            ORDER BY sum_amount DESC;"""

