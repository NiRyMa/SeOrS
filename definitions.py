import sqlite3
import datetime
import random
import os
import sys

connection = sqlite3.connect("table.db")
cursor = connection.cursor()
def all_transactions():
    cursor.execute(f'SELECT * FROM transactions')
    data = cursor.fetchall()
    for i in range(len(data)):
        print(data[i][0],"\t",data[i][1],"\t",data[i][2],"\t",data[i][3],"\t",data[i][4])
def relocation(data, name):
    id_recipient = int(data.split()[0])
    summa = int(data.split()[1])
    cursor.execute(f'SELECT id FROM users WHERE name="{name}"')
    id_sender = int(cursor.fetchall()[0][0])
    transaction(id_recipient, id_sender, summa)
    print("Операция успешно проведена!")

def delete(name):
    if input("Вы уверены что хотите удалить свой аккаунт?(Да/Нет)")=="Да":
        cursor.execute(f'DELETE FROM users WHERE name="{name}"')
        connection.commit()
        print("Было приятно с вами работать!")

def balance(my_name):
    cursor.execute(f"SELECT balance FROM users WHERE name='{my_name}'")
    print("Ваш баланс:", cursor.fetchall()[0][0])

def users():
    cursor.execute("SELECT id, name FROM users")
    data = cursor.fetchall()
    print("id\tname")
    for i in range(len(data)):
        print(data[i][0],"\t",data[i][1])

def black_list():
    cursor.execute("SELECT name FROM black_list")
    black_list = cursor.fetchall()
    for i in range(len(black_list)):
        black_list[i] = black_list[i][0]
    return black_list

def white_list():
    cursor.execute("SELECT name FROM white_list")
    white_list = cursor.fetchall()
    for i in range(len(white_list)):
        white_list[i] = white_list[i][0]
    return white_list

def transaction(id_recipient, id_sender, summa):
    new_transaction = (random_id(), id_recipient, id_sender, summa, datetime.datetime.now())
    cursor.execute('''INSERT INTO transactions (id,id_recipient,id_sender,sum_of_transaction,time_transaction) VALUES (?, ?, ?, ?, ?);''',new_transaction)
    connection.commit()
    cursor.execute(f'SELECT balance FROM users WHERE id ={id_recipient}')
    data = cursor.fetchall()
    data  = int(data[0][0]) - summa
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (data, id_recipient))
    connection.commit()
    cursor.execute(f'SELECT balance FROM users WHERE id ={id_sender}')
    data = cursor.fetchall()
    data  = int(data[0][0]) + summa
    cursor.execute("UPDATE users SET balance = ? WHERE id = ?", (data, id_sender))
    
def random_black_name():
    cursor.execute("SELECT name FROM black_list")
    data =cursor.fetchall()
    for i in range(len(data)):
        data[i] = data[i][0]
    data+=["VVP","IVJ","AIH","MDD","PP"]
    data = list(set(data))
    return data[random.randint(0,len(data)-1)]

def random_white_name():
    cursor.execute("SELECT name FROM white_list")
    data =cursor.fetchall()
    for i in range(len(data)):
        data[i] = data[i][0]
    data+=["AAN","BEN","IYV","AAS","ANR"]
    data = list(set(data))
    return data[random.randint(0,len(data)-1)]

def unique_user(number):
    number = (number,)
    cursor.execute("SELECT id FROM users")
    data = cursor.fetchall()
    cursor.execute("SELECT id FROM transactions")
    data +=cursor.fetchall()
    if number in data:
        return 0
    else:
        return 1

def random_id():
    rand = random.randint(0,2**16)
    while not unique_user(rand):
        rand = random.randint(0,2**16)
    return rand

def new_white():
    new_white = (random_id(),random_white_name()) 
    cursor.execute('''INSERT INTO white_list (id,name) VALUES (?, ?);''',new_white)
    connection.commit()

def new_user(name):
    new_users = (random_id(), name,random.randint(0,10000))
    cursor.execute('''INSERT INTO users (id, name, balance) VALUES (?, ?, ?);''',new_users)
    connection.commit()

def new_black():
    new_black = (random_id(), random_black_name())
    cursor.execute('''INSERT INTO black_list (id, name) VALUES (?, ?);''',new_black)
    connection.commit()
