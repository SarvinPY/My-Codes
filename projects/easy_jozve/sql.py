import sqlite3
database = sqlite3.connect("E:\\code\\projects\\easy_jozve\\first.db")
cur = database.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
        name TEXT , 
        last TEXT ,
        age INT
            );""")
cur.execute("""INSERT INTO first(name, last, age)
            VALUES('sarvin', 'Hosseini', 20);""")
database.commit()
database.close()