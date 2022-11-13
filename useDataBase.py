import sqlite3

# class DBmanager:
#     def __init__(db_file):
#         conn = sqlite3.connect(db_file)
#         cursor = conn.cursor()

#     def add_user(user_name):
#         cursor.execute("INSERT INTO 'records'('name') VALUES (?)", (user_name,)) 
#         conn.commit()

#     def show():
#         db = cursor.execute("SELECT * FROM 'records'")
#         print(db.fetchall())

def connect():
    try:
        conn = sqlite3.connect("PyDB2.db")
        cursor = conn.cursor()
        #Считывание пользователей
        users = cursor.execute("SELECT * FROM 'users'")
        # print(users.fetchall())
        return ("DataBase connected!")
    except sqlite3.Error as error:
        print("Error - ", error)
        return (f"Error - {error} 😭")
    finally:
        if(conn):
            conn.close()

# def add_user(user_name):
#     cursor.execute("INSERT INTO 'records'('name') VALUES (?)", (user_name,)) 
#     conn.commit()



# try:
#     conn = sqlite3.connect("PyDB2.db")
#     cursor = conn.cursor()

#     #Считывание пользователей
#     users = cursor.execute("SELECT * FROM 'users'")
#     print(users.fetchall())

#     conn.commit()

# except sqlite3.Error as error:
#     print("Error - ", error)
# finally:
#     if(conn):
#         conn.close()


            # if message.text == "DB":
    #     try:
    #         conn = sqlite3.connect("PyDB2.db")
    #         cursor = conn.cursor()
            
    #         #создание пользователя с user_id  = 1000
    #         cursor.execute("INSERT OR IGNORE INTO 'users' ('user_id') VALUES(?)", (2000,))

    #         #Считывание пользователей
    #         users = cursor.execute("SELECT * FROM 'users'")
    #         print(users.fetchall())

    #         conn.commit()

    #     except sqlite3.Error as error:
    #         bot.send_message("Error - ",error)
    #     finally:
    #         if(conn):
    #             conn.close()