import os
import sqlite3

os.system('cls')
conn = sqlite3.connect('test.sqlite3')

# cursor.fetchall
print('\nusing fetchall', '='*50)
cursor = conn.execute("select * from table01;")
rows = cursor.fetchall()
print(rows)

for row in rows:
    print('{}\t{}'.format(row[0], row[1]))

# cursor.fetchone
print('\nusing fetchone', '='*50)
cursor = conn.execute("select * from table01;")
row_one = cursor.fetchone()
print(row_one)
print('{}\t{}'.format(row_one[0], row_one[1]))

conn.close()
