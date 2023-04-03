import sqlite3

conn = sqlite3.connect('company.db')
print("Successfully connected to the database")

data = conn.execute("SELECT * FROM Company2")
for rows in data:
    print('ID=', rows[0])
    print('firstname=', rows[1])
    print('Lastname= ', rows[2])
    print('Age=', rows[3])
    print('Salary ', rows[4])
    print('Task ', rows[5])

print("Selected records")
conn.close
