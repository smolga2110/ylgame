import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()
result = cur.execute('''SELECT score FROM user''').fetchall()
print(result[0][0])

