import sqlite3

conn = sqlite3.connect('company.db')
print("Succesfully connected to the database")

conn.execute("DELETE FROM Company2 where ID=4")
conn.commit()

data = conn.execute("SELECT * FROM Company2")
for rows in data:
    print("ID:", rows[0])
    print("FIRSTNAME", rows[1])
    print("LASTNAME", rows[2])
    print("AGE:", rows[3])
    print("SALARY", rows[4])
    print("TASK:", rows[5])

print("Successfully deleted one row")
conn.close()