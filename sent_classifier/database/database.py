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


def create_hotel_table():
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
        print("Hotels table created successlly")
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
        print("Hotel inserted successfully")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)


def get_hotels():
    global records
    try:
        connection = create_connection()
        cursor = connection.cursor()
        get_query = '''SELECT id, name, reviews, link FROM hotel
        '''
        cursor.execute(get_query)
        records = cursor.fetchall()
        close_connection(connection)
        return records
    except (Exception, Error) as error:
        print("Error: ", error)


def create_review_table():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS review
        (ID SERIAL PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,   
        HOTEL TEXT NOT NULL,
        REVIEW TEXT NOT NULL,
        DATE TEXT NOT NULL,
        UNIQUE (REVIEW));
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Review Table created successfully")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)


def insert_review(title, hotel, review, date):
    try:
        create_review_table()
        connection = create_connection()
        cursor = connection.cursor()
        insert_query = '''INSERT INTO  review (NAME, HOTEL, REVIEW, DATE) VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert_query, (title, hotel, review, date))
        connection.commit()
        print("Review inserted successfully")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)


if __name__ == '__main__':
    insert_hotel()
    get_hotels()
    insert_review()
