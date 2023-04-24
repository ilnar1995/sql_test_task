import sqlite3
from sqlite3 import Error
import pathlib

def print_table(teams_list, data):
    row_format = "{:>16}" * (len(teams_list))
    print(row_format.format(*teams_list))
    for row in data:
        print(row_format.format(*row))
def create_connection(path, name_db):
    connection = None
    try:
        connection = sqlite3.connect(path + "/" + name_db)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def create_table(connection):
    create_employee_table = """
        CREATE TABLE IF NOT EXISTS employee(
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          name VARCHAR(255) NOT NULL
        );
        """
    create_sales_table = """
        CREATE TABLE IF NOT EXISTS sales(
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          employee_id INTEGER NOT NULL, 
          price INTEGER NOT NULL, 
          FOREIGN KEY (employee_id) REFERENCES employee (id)
        );
        """
    execute_query(connection, create_employee_table)
    execute_query(connection, create_sales_table)


def create_fields(connection):
    query1 = """
    INSERT INTO "employee" ("name") VALUES ('%s')
    """
    query2 = """
    INSERT INTO "sales" ("price", "employee_id") VALUES (%s, %s)
    """
    execute_query(connection, query1 % ("Алена"))
    execute_query(connection, query1 % ("Сергей"))
    execute_query(connection, query1 % ("Николай"))
    execute_query(connection, query2 % (1000, 1))
    execute_query(connection, query2 % (50, 1))
    execute_query(connection, query2 % (100, 1))
    execute_query(connection, query2 % (200, 1))
    execute_query(connection, query2 % (400, 2))
    execute_query(connection, query2 % (10, 2))
    execute_query(connection, query2 % (30, 2))
    execute_query(connection, query2 % (90, 2))
    execute_query(connection, query2 % (400, 3))
    execute_query(connection, query2 % (10, 3))
    execute_query(connection, query2 % (20, 3))
    execute_query(connection, query2 % (10, 3))
    execute_query(connection, query2 % (15, 3))



if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.resolve()
    connection = create_connection(str(path), "db.sqlite3")
    create_table(connection)
    # create_fields(connection)
    query = """
        SELECT 
            "employee"."id", 
            "employee"."name", 
            COUNT("employee"."id") AS "sales_c", 
            RANK() OVER (ORDER BY COUNT("employee"."id") DESC) AS "sales_rank_c", 
            SUM("sales"."price") AS "sales_s", 
            RANK() OVER (ORDER BY SUM("sales"."price") DESC) AS "sales_rank_s"
        FROM "employee" 
        LEFT OUTER JOIN "sales" ON ("employee"."id" = "sales"."employee_id") GROUP BY "employee"."id", "employee"."name" 
        ORDER BY "employee"."id" ASC
    """

    users = execute_read_query(connection, query)

    teams_list = ['id', 'name', 'seles_c', 'seles_rank_c', 'sales_s', 'sales_rank_s']

    print_table(teams_list, users)

    # create_connection('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
