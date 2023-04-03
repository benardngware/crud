import sqlite3

conn = sqlite3.connect('company.db')
print("Successfully connected to database")

conn.execute("DELETE FROM Company1 WHERE ID = 5; ")

conn.commit()
print("Successfully deleted last row")

conn.close()