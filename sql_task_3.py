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
        CREATE TABLE IF NOT EXISTS transfers(
          id INTEGER PRIMARY KEY AUTOINCREMENT, 
          'from' INTEGER NOT NULL, 
          'to' INTEGER NOT NULL, 
          amount INTEGER NOT NULL, 
          tdate DATE NOT NULL
        );
        """
    execute_query(connection, create_employee_table)


def create_fields(connection):
    query = """
    INSERT INTO "transfers" ("from", "to", "amount", "tdate") VALUES (%s, %s, %s, "%s")
    """
    execute_query(connection, query % (1, 2, 500, '2023-02-23'))
    execute_query(connection, query % (2, 3, 300, '2023-03-01'))
    execute_query(connection, query % (3, 1, 200, '2023-03-05'))
    execute_query(connection, query % (1, 3, 400, '2023-04-05'))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.resolve()
    connection = create_connection(str(path), "db.sqlite3")
    create_table(connection)
    # create_fields(connection)

    query = """
    SELECT 
        user as acc,
        tdate as balance,
       COALESCE((SELECT MIN(t2.tdate)
        FROM (
                SELECT `from` as `user`, amount*-1 as `change`, tdate FROM transfers UNION ALL
                SELECT `to` as `user`, amount as `change`, tdate FROM transfers
        ) as t2
        WHERE t2.user = t.user and t2.tdate > t.tdate
       ),'3000-01-01') as dt_to,
       (SELECT sum(t2.change)
        FROM (
                SELECT `from` as `user`, amount*-1 as `change`, tdate FROM transfers UNION ALL
                SELECT `to` as `user`, amount as `change`, tdate FROM transfers
        ) as t2
        WHERE t2.user = t.user and t2.tdate <= t.tdate
       ) as dt_from
    FROM (
            SELECT `from` as `user`, amount*-1 as `change`, tdate FROM transfers UNION ALL
            SELECT `to` as `user`, amount as `change`, tdate FROM transfers
    ) as t
    ORDER BY `user`, tdate ASC;
    """

    q = """
    select * from transfers
    """
    quweryset = execute_read_query(connection, query)

    # print(quweryset)
    teams_list = ['acc', 'dt_from', 'dt_to', 'balance']
    print_table(teams_list, quweryset)
    #print(quweryset)


