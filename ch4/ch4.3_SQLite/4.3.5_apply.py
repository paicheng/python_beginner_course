import os
import sqlite3


def menu():
    os.system("cls")
    print("account management system")
    # print("="*50)
    print("=" * 50 + """
    1. create new account
    2. display account and password
    3. modify password
    4. delete account
    0. terminate system""")
    print("="*50)


def new_account():
    while True:
        name = input('new name: ')
        if name == '':
            break

        # conn = sqlite3.connect(db_path)
        cursor = conn.execute("select name from password")
        names = cursor.fetchall()
        if name in names:
            print("{} is existed.".format(name))
            continue

        password = input("input the password: ")
        conn.execute(
            "insert into password (name, pass) values('{}', '{}')".format(name, password))
        conn.commit()
        # conn.close()
        break


def show_account():
    # conn = sqlite3.connect(db_path)
    sql = "select * from password"
    cursor = conn.execute(sql)
    rows = cursor.fetchall()
    if rows != None:
        os.system('cls')
        print("{}\t{}\t{}".format("id", "name", "password"))
        print("="*50)
    for row in rows:
        print("{}\t{}\t{}".format(row[0], row[1], row[2]))
    # conn.close()
    input("any key back to menu")


def update_pass():
    while True:
        name = input("input name: ")
        if name == "":
            break

        # conn = sqlite3.connect(db_path)
        sql = "select name, pass from password where name = '{}'".format(name)
        cursor = conn.execute(sql)
        record = cursor.fetchone()
        if record:
            oldpass = input("input your password: ")
            if oldpass == record[1]:
                password = input("new password: ")
                sql = """
                    UPDATE password 
                    SET pass = '{}' 
                    WHERE name = '{}'
                    """.format(password, name)
                conn.execute(sql)
                conn.commit()
                print("\n" + "="*50)
                print("password in modified.")
                input("any key back to menu")
                break


def delete_account():
    while True:
        name = input("name: ")
        if name == "":
            break

        sql = "SELECT name, pass FROM password WHERE name = '{}'".format(name)
        cursor = conn.execute(sql)
        record = cursor.fetchone()
        if record == None:
            print("{} is not existed".format(name))
            continue
        else:
            while True:
                pw = input("password: ")
                if pw == "":
                    break
                elif pw == record[1]:
                    sql = "DELETE FROM password WHERE name = '{}'".format(name)
                    conn.execute(sql)
                    conn.commit()
                    print("{} is deleted.".format(name))
                    input("any key to menu")
                    break
            break


dirname = os.path.dirname(__file__)
db_path = os.path.join(dirname, 'sqlite.sqlite3')
if not os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    sql = """
        CREATE TABLE IF NOT EXISTS password(
            'id' integer primary key not null
            , 'name' text not null unique
            , 'pass' text not null
        )
        """
    conn.execute(sql)

    sql = """
        INSERT INTO password (name, pass) 
        VALUES('alan', 'alan'), ('bill', 'bill'), ('candy', 'candy')
        """
    conn.execute(sql)
    conn.commit()

while True:
    menu()
    choice = int(input("input your choice: "))
    if choice == 1:
        new_account()
    elif choice == 2:
        show_account()
    elif choice == 3:
        update_pass()
    elif choice == 4:
        delete_account()
    elif choice == 0:
        break

conn.close()
