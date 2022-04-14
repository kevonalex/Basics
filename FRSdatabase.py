import sqlite3
#conn = sqlite3.connect('':memory:'') # creates temprary data storage
conn = sqlite3.connect('filmarchive.db') # creates a variable to connect to the database

c = conn.cursor()

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

#FILMS NOW SHOWING
#list_films = [
#                (2, 'Fantastic Beasts: The Secrets of Dumbledore', 12, '1hr56mins', 'TBC'),
#                (3, 'Sonic The Hedgehog 2', 0, '1hr56mins', 'TBC'),
#                (4, 'Morbius', 15, '1hr56mins', 'TBC'),
#                (5, 'The Bad Guys', 0, '1hr56mins', 'TBC'),
#                (6, 'Rabbit Academy', 0, '1hr56mins', 'TBC'),
#             ]

#PT.1  TABLE GENERATION
# create table to store films
#c.execute("""CREATE TABLE filminfo(
#    screen_no integer,
#    title text,
##    age_restriction integer,
#    runtime text,
#    rating integer
#)""")

#PT.3 QUERY/FETCH + FORMATTING
#c.execute("SELECT * FROM filminfo") # sets query
#fetch options
#c.fetchone()
#c.fetchmany()
#films_list = c.fetchall()
#for film in films_list:
#    print('\n'+film[1])
#c.executemany("INSERT INTO filminfo VALUES (?,?,?,?,?)", list_films)

#PT.4 PRIMARY KEY
# IDEA:
#c.execute("SELECT rowid,  * FROM filminfo") # sets query

#films_list = c.fetchall()

#for film in films_list:
#    print(film)
#print("COMMAND SUCCESSFUL")

#PT.5 WHERE CLAUSE
#c.execute("SELECT * FROM filminfo WHERE age_restriction > 12") # sets database query to find film

#films_list = c.fetchall()

#for film in films_list:
#    print(film)

#print("COMMAND SUCCESSFUL")

#PT.6 UPDATE RECORDS
#c.execute("""UPDATE filminfo SET title = 'The Batman'
#            WHERE screen_no = 1
#""") # sets database query to find film

#PT.7 DELETE RECORDS
#c.execute("DELETE from filminfo WHERE rowid = <ENTER ROWID HERE>")

#PT.8 ORDER RESULTS
#c.execute("SELECT rowid, * FROM filminfo ORDER BY title DESC")

#PT.9 AND/OR
#c.execute("SELECT * FROM filminfo WHERE age_restriction = '12' OR title LIKE 'M%'")

#PT.10 LIMITS
#c.execute("SELECT * FROM filminfo ORDER BY screen_no DESC LIMIT 4") #add limits to end for large datasets

#PT.11 DROP table
#c.execute("DROP TABLE <ENTER TABLE NAME HERE>")
#conn.commit()

films_list = c.fetchall()

for film in films_list:
    print(film)

print("COMMAND SUCCESSFUL")

conn.commit()
# close connection
conn.close()
