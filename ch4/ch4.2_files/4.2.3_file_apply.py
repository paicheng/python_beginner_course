import os
import ast


def menu():
    os.system('cls')
    print('account/password mgnt system')
    print('='*50)
    print('''
    1. input account and password
    2. display account and password
    3. change account and password
    4. remove account and password
    0. End''')
    print("="*50)


def read_data():
    mypath = os.path.join(par_dir, 'password.txt')
    with open(mypath, 'r', encoding='utf-8') as f:
        filedata = f.read()
        if filedata != '':
            data = ast.literal_eval(filedata)
            return data
        else:
            return dict()


def display_data():
    print('account\tpassword')
    print('='*50)
    for key in data:
        print('{}\t{}'.format(key, data[key]))
    input('any key back to menu')


def input_data():
    while True:
        name = input('name')
        if name == "":
            break
        if name in data:
            print('{} is existed.'.format(name))
            continue
        password = input('password')
        data[name] = password
        mypath = os.path.join(par_dir, 'password.txt')
        with open(mypath, 'w', encoding='utf-8') as f:
            f.write(str(data))
            print('{} is saved'.format(name))
            break


def edit_data():
    while True:
        name = input('name')
        if name == '':
            break
        if not name in data:
            print("{} account is not existed")
            continue
        print('old password is {}'.format(data[name]))
        password = input('new password')
        data[name] = password
        mypath = os.path.join(par_dir, 'password.txt')
        with open(mypath, 'w', encoding='utf8') as f:
            f.write(str(data))
            input('password is renewed')
            break


def delete_data():
    while True:
        name = input('input name')
        if name == '':
            break
        if not name in data:
            print('{} is not existed'.format(name))
            continue
        print('Are you sure to delete account {}?'.format(name))
        yn = input("(Y/N)?")
        if yn == 'Y' or yn == 'y':
            del data[name]
            mypath = os.path.join(par_dir, 'password.txt')
            with open(mypath, 'w', encoding='utf8') as f:
                f.write(str(data))
                print('{} is removed'.format(name))
                input('any key back to menu')
                break


current_dir = os.path.dirname(__file__)
par_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
data = read_data()
while True:
    menu()
    choice = int(input('your choice? '))
    if choice == 1:
        input_data()
    elif choice == 2:
        display_data()
    elif choice == 3:
        edit_data()
    elif choice == 4:
        delete_data()
    else:
        break
print("system terminated")
