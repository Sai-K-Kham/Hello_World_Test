def hours():
    print('Open 9-5 daily')

import csv
with open('books.csv', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)

import sqlite3
conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books (title VARCHAR(20) PRIMARY KEY, author VARCHAR(20), year INT)''')
curs.execute('INSERT INTO books VALUES("The Weirdstone of Brisingamen","Alan Garner",1960)')
curs.execute('INSERT INTO books VALUES("Perdido Street Station","China Miéville", 2000)')
curs.execute('INSERT INTO books VALUES("Thud!","Terry Pratchett",2005)')
curs.execute('INSERT INTO books VALUES("The Spellman Files","Lisa Lutz", 2007)')
curs.execute('INSERT INTO books VALUES("mall Gods","Terry Pratchett", 1992)')

print(curs.execute('SELECT title FROM books ORDER BY ASC'))

import sqlalchemy as sa
conn = sa.create_engine('sqlite:///books.db')
result = conn.execute(books.select('title'))
