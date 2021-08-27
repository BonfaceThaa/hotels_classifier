import os

import psycopg2
from psycopg2 import Error


def create_connection():
    """
    Function creating connection to database
    :return: connection database connection object
    """
    connection = psycopg2.connect(user=os.environ.get('HOTEL_CLASSIFIER_DB_USER'),
                                  password=os.environ.get('HOTEL_CLASSIFIER_DB_PASS'),
                                  host=os.environ.get('HOTEL_CLASSIFIER_DB_HOST'),
                                  port=os.environ.get('HOTEL_CLASSIFIER_DB_PORT'),
                                  database=os.environ.get('HOTEL_CLASSIFIER_DB'))
    print("DB USER:", os.environ.get('HOTEL_CLASSIFIER_DB_USER'))
    return connection


def close_connection(connection):
    """
    Function accepting a database connection and closing it
    :param connection: database connection object
    """
    if connection:
        connection.close()


def create_hotel_table():
    """Function to create hotel table"""
    try:
        connection = create_connection()
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS hotel
        (ID SERIAL PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        REVIEWS TEXT NOT NULL,
        RATING INT,
        LINK TEXT,
        STATUS BOOLEAN DEFAULT 'no');
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Hotels table created successfully")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)


def insert_hotel(name, link, reviews):
    """
    Function to insert hotel
    :param name: name of hotel
    :param link: detail page of hotel
    :param reviews: review of hotel
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        insert_query = '''INSERT INTO  hotel (NAME, REVIEWS, LINK) VALUES (%s, %s, %s)'''
        cursor.execute(insert_query, (name, link, reviews))
        connection.commit()
        print("Hotel inserted successfully")
        close_connection(connection)
    except (Exception, Error) as error:
        print("Error: ", error)


def get_hotels():
    """
    Function to fetch all hotels that have not been scrapped
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        get_query = '''SELECT id, name, reviews, link FROM hotel WHERE status IS NOT TRUE'''
        cursor.execute(get_query)
        records = cursor.fetchall()
        close_connection(connection)
        return records
    except (Exception, Error) as error:
        print("Error: ", error)


def update_hotel_status(id, status):
    """
    Function to update the scrapped status of a hotel
    :param id: id of a hotel
    :param status: completed scrapped status
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        update_query = '''UPDATE hotel SET status = %s WHERE id = %s'''
        cursor.execute(update_query, (status, id))
        connection.commit()
        print("Record updated successfully")
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)


def create_review_table():
    """
    Function to create review table
    """
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
    """
    Function to insert a review
    :param title: title of review
    :param hotel: hotel that the review targets
    :param review: review text
    :param date: year and month of review
    """
    try:
        create_review_table()
        connection = create_connection()
        cursor = connection.cursor()
        insert_query = '''INSERT INTO  review (NAME, HOTEL, REVIEW, DATE) VALUES (%s, %s, %s, %s)'''
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
    update_hotel_status()
