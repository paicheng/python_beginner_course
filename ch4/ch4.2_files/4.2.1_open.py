import os

content = '''Hello Python
中文字測試
Welcome
'''

# write into file
f = open('file1.txt', 'w',  encoding='utf-8')
f.write(content)
f.close()

# read from file
f = open('file1.txt', 'r')
for line in f:
    print(line, end='')
f.close()

# using with
with open('file1.txt', 'r') as f:
    for line in f:
        print(line, end='')
