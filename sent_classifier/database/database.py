import psycopg2
from psycopg2 import Error


def create_connection():
    connection = psycopg2.connect(user='postgres',
                                  password='4212',
                                  host='localhost',
                                  port='5432',
                                  database='hotels')
    return connection


def close_connection(connection):
    if connection:
        connection.close()


def create_table():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS hotel
        (ID SERIAL PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        REVIEWS TEXT NOT NULL,
        RATING INT,
        LINK TEXT);
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successlly")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)


def insert_hotel(name, link, reviews):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        insert_query = '''INSERT INTO  hotel (NAME, REVIEWS, LINK) VALUES (%s, %s, %s)
        '''
        cursor.execute(insert_query, (name, link, reviews))
        connection.commit()
        print("Item inserted successfully")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)

get


if __name__ == '__main__':
    insert_hotel()
