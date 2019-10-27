import os

os.system("cls")
with open('yourFile.txt', 'r') as f:
    string = f.read()
    print(string)
    print("="*20)

    f.seek(0)
    string = f.read(5)
    print(string)
    print("="*20)

    f.seek(0)
    content = f.readlines()
    print(content)
    print("="*20)

    f.seek(0)
    content = f.readline()
    print(content)
    print("="*20)
