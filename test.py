import sqlite3
import json

conn = sqlite3.connect('test.db')
cur = conn.cursor()
lst = [1, 2, 3, 4, 'q']
tmp = json.dumps(lst)

cur.execute('insert into tbl values(?)', (tmp,))
conn.commit()
cur.execute('select * from tbl')
data = cur.fetchall()
for line in data:
    print(json.loads(line[0]))
