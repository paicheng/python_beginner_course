import sqlite3

conn = sqlite3.connect('test.sqlite3')
# conn = conn.conn()

# CREATE TABLE
sql = """
    CREATE TABLE IF NOT EXISTS table01(
        'id' integer primary key not null
        , 'tel' text
    )
"""
conn.execute(sql)
conn.execute('DELETE FROM table01')
conn.commit()

# INSERT
sql = 'INSERT INTO table01 VALUES(1, "02-1234567"), (2, "04-7654321"), (3,"03-9567789")'
conn.execute(sql)

# UPDATE
sql = "UPDATE table01 SET tel = '04-1234567' WHERE id = 2"
conn.execute(sql)

# DELETE
sql = "DELETE FROM table01 WHERE id = 3"
conn.execute(sql)

conn.commit()
conn.close()
