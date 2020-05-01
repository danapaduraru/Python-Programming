import sqlite3

# look for: chinook sqlite
# https://www.sqlitetutorial.net/sqlite-sample-database/
# https://github.com/wblakecannon/DataCamp/blob/master/05-importing-data-in-python-(part-1)/_datasets/Chinook.sqlite

conn = sqlite3.connect('test.db')
curs = conn.cursor()
curs.execute('select * from customers')
curs.fetchone()
curs.fetchall()  # toate rezultatele intr-o lista
for row in curs:
    print(row)

# not so good: permite sql injection
# l = "input extern"
# s = "select * from customers where something like '{}%'"
# curs.execute(s.format(l))
# sau
"""
curs.execute(s, (l, ))
sau dictionar unde dam valorile variabilelor!!
"""

s = 'insert into t values(?,?,?)'
curs.execute(s, ('a','b','c'))
conn.commit()

curs.executemany(s, [('a','b'),(...),(....)])

# ORMS FOR PYTHON
# peewee
# SqlAlchemy - mai complex
