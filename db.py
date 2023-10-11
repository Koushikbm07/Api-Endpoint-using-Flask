import sqlite3


conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE  IF EXISTS users')
cursor.execute(''' 
               CREATE TABLE  users(
                    id INTEGER PRIMARY KEY AUTO INCREMENT,
                    name  TEXT  NOT NULL,
                    age  INTEGER NOT NULL 
                )''')

conn.commit()
conn.close()