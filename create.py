import sqlite3

def function_create():
    connection = sqlite3.connect("table.db")
    cursor = connection.cursor()

    transaction_db = '''
    CREATE TABLE IF NOT EXISTS transactions (
        id integer primary key,
        id_recipient integer not null,
        id_sender integer not null,
        sum_of_transaction float,
        time_transaction date
    );'''
    cursor.execute(transaction_db)
    connection.commit()
    black_list_db = '''
    CREATE TABLE IF NOT EXISTS black_list (
        id integer primary key,
        name VARCHAR(255) not null
        );
    '''
    cursor.execute(black_list_db)
    connection.commit()
    white_list_db = '''
    CREATE TABLE IF NOT EXISTS white_list (
        id integer primary key,
        name VARCHAR(255) not null
        );
    '''
    cursor.execute(white_list_db)
    connection.commit()
    users_db = '''
    CREATE TABLE IF NOT EXISTS users (
        id integer primary key,
        name VARCHAR(255),
        balance float
        );
    '''
    cursor.execute(users_db)
    connection.commit()
