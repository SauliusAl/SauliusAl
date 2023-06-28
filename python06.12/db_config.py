import psycopg2
from psycopg2._psycopg import cursor, connection

db_params = {
        'host': 'localhost',
        'port': 5432,
        'database': 'real_estate',
        'user': 'postgres',
        'password': 'sale72'
    }
def create_table():

    connection = psycopg2.connect(**db_params)  #perduodam dictionary reiksmes i connection - su **

    create_table_query = """
    CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    kaina INTEGER,
    lokacija VARCHAR(255),
    plotas VARCHAR (255)
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)

    connection.commit()

    cursor.close()
    connection.close()

def insert_data(data):
    connection = psycopg2.connect(**db_params)

    cursor = connection.cursor()

    insert_table = """
    INSERT INTO properties (kaina, lokacija, plotas)
    VALUES (%s, %s, %s)
    """

    cursor.executemany(insert_table, data)
    connection.commit()

    cursor.close()
    connection.close()

def ikelti_duomenis():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    select_query = """
    SELECT kaina, lokacija, plotas FROM properties
    """
    cursor.execute(select_query)

    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows