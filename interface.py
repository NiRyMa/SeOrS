from generate import *

if not os.path.exists(os.getcwd()+"/flag.txt"): 
    try:
        generate_data()
    except:
        generate_data()
    file = open("flag.txt", "w+")
    file.write("Hello")
    file.close()

role = input("Выберите роль - Администратор(1) или Пользователь(0):")
try:
    int(role)
except:
    print("Хорошая попытка, но нет")
    sys.exit()

if int(role):
    name = input("Введите ваше имя, Администратор:")
    if name in black_list():
        print("Извините, но вы заблокированы, попробуйте другой псевдоним")
    else:
        exit_ = 0
        new_user(name)
        while not exit_:
            print(f'Здравствуйте {name}, так как вы администратор у вас есть следующие возможности:')
            print("1)Список пользователей\n2)Блокировка пользователей")
            print("3)Ваш баланс\n4)Обмен валютой с любым пользователем\n5)Список почета")
            print("6)Черный список\n7)Добавить пользователя в список почета\n8)Удаление аккаунта\n9)Список транзакций")
            request = input("Введите номер опции или exit для выхода:")
            if request == "exit":
                print("Приятно было с вами работать!")
                break
            elif request not in "123456789":
                print("Вы ввели несуществующию опцию!")
            else:
                match request:
                    case "1":
                        users()
                    case "2":
                        data = input("Для блокирвоки пользователя введите его id, для возвращения в прошлое меню - пустую строку")
                        if data!="":
                            data = int(data)
                            cursor.execute(f'SELECT name FROM users WHERE id = "{data}"')
                            tmp = cursor.fetchall()[0][0]
                            cursor.execute('''INSERT INTO black_list (id, name) VALUES(?, ?)''',(data,tmp))
                            connection.commit()
                            cursor.execute(f'DELETE FROM users WHERE id="{data}" AND name="{tmp}"')
                            connection.commit()
                    case "3":
                        balance(name)
                    case "4":
                        data = input("Введите id пользователя и сумму которую хотите ему отправить через пробел(если хотите получить то введите эту же сумму со знаком минус или пустую строку для возвращения в прошлое меню")
                        if data!="":
                            relocation(data, name)
                    case "5":
                        white_list = white_list()
                        for i in range(len(white_list)):
                            print(white_list[i])
                    case "6":
                        black_list = black_list()
                        for i in range(len(black_list)):
                            print(black_list[i])
                    case "8":
                        delete(name)
                        break
                    case "7":
                        data = input("Для почтения пользователя введите его id, для возвращения в прошлое меню - пустую строку")
                        if data!="":
                            data = int(data)
                            cursor.execute(f'SELECT name FROM users WHERE id = {data}')
                            tmp = cursor.fetchall()[0][0]
                            cursor.execute('''INSERT INTO white_list (id, name) VALUES(?, ?)''',(data,tmp))
                            connection.commit()
                    case "9":
                        all_transactions()
elif not int(role):
    name = input("Введите ваше имя, Пользователь:")
    if name in black_list():
        print("Извините, но вы заблокированы, попробуйте другой псевдоним")
    else:
        exit_=0
        new_user(name)
        while not exit_:
            print(f'Здравствуйте {name}, так как вы пользователь у вас есть следующие возможности:')
            print("1)Список всех пользователей\n2)Ваш баланс\n3)Обмен валютой с любым пользователем")
            print("4)Список почета\n5)Удаление аккаунта\n")
            request = input("Введите номер опции или exit для выхода:")
            if request == "exit":
                print("Приятно было с вами работать!")
                break
            elif request not in "12345":
                print("Вы ввели несуществующию опцию!")
            else:
                match request:
                    case "1":
                        users()
                    case "2":
                        balance(name)
                    case "3":
                        data = input("Введите id пользователя и сумму которую хотите ему отправить(если хотите получить то введите эту же сумму со знаком минус или пустую строку для возвращения в прошлое меню")
                        if data!="":
                            relocation(data, name)
                    case "4":
                        white_list = white_list()
                        for i in range(len(white_list)):
                            print(white_list[i])
                    case "5":
                        delete(name)
                        break
