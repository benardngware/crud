import sqlite3

conn = sqlite3.connect('company.db')
print("Successfully opened database")

# crud
conn.execute("""CREATE TABLE Company2(
ID INT PRIMARY KEY #IDSHOULDBEDIFFERENTINEACH ROW NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL ,
AGE INT,
SALARY REAL,
TASK TEXT CHAR(20))""")

print("Successfully Created Company1 table")
conn.close()
