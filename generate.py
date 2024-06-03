from create import *
from definitions import *

def generate_data():
    
    function_create()
    connection = sqlite3.connect("table.db")
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM users")
    users = cursor.fetchall()
    for i in range(len(users)):
        users[i] = users[i][0]
    for j in range(200):
        new_user("NPC"+str(random_id()))
    for k in range(5):
        new_black()
    for l in range(5):
        new_white()
    for _ in range(250):
        id_recipient = users[random.randint(0,len(users)-1)]
        id_sender = users[random.randint(0,len(users)-1)]
        summa = random.randint(0,50000)
        transaction(id_recipient, id_sender, summa)
    cursor.close()
    connection.close()
