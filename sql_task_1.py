import sqlite3
from sqlite3 import Error
import pathlib

def create_connection(path, name_db):
    connection = None
    try:
        connection = sqlite3.connect(path + "/" + name_db)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



if __name__ == '__main__':
    path = pathlib.Path(__file__).parent.resolve()
    connection = create_connection(str(path), "db.sqlite3")

    query = """
        WITH RECURSIVE dates(date) AS (
          VALUES(date('now'))
          UNION ALL
          SELECT date(strftime('%s', date) +
                abs(random() % (strftime('%s', '2000-01-06 23:59:59') -
                                strftime('%s', '2000-01-01'))
                   ) + 
                   strftime('%s', '2000-01-03') -
                   strftime('%s', '2000-01-01'),
                'unixepoch')
          FROM dates
          LIMIT 100
        )
        SELECT date FROM dates;
    """

    users = execute_read_query(connection, query)

    print(users)

    # create_connection('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
