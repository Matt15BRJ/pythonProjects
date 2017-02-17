#creates a temporary database, fills it with some data,
#then selects and prints out names and IQ's for the humans
#Practice with Python3 and Sqlite3
import sqlite3

values = (
    ('Jean-Baptiste Zorg', 'Human', '122'),
    ('Korben Dallas', 'Meat Popsicle', '100'),
    ("Ak'not","Mangalore",'-5')
    )

with sqlite3.connect(':memory:') as connection:
    c=connection.cursor()
    c.executescript("""
    DROP TABLE IF EXISTS Sentients;
    CREATE TABLE Sentients(Name TEXT, Species TEXT, IQ INT);
    """)
    c.executemany("INSERT INTO Sentients VALUES(?,?,?)",values)#populates table with values from 'values' tuple of tuples
    c.execute("UPDATE Sentients SET Species=('Human') WHERE Name=('Korben Dallas')")
    c.execute("SELECT Name, IQ FROM Sentients WHERE Species = ('Human')")
    for row in c.fetchall():
        print('Name: {}, IQ: {}'.format(row[0],row[1]))
              

        
