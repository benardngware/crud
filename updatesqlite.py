import sqlite3

con = sqlite3.connect('company.db')
print("Successfully connected to database")

con.execute("UPDATE Company2 set SALARY = 50000.00 WHERE ID = 4; ")
# TO SAVE THE CHANGE
con.commit()
print("Successfully updated")



data= con.execute("SELECT * FROM Company2")
for rows in data:
    print("ID:", rows[0])
    print("FIRSTNAME:", rows[1])
    print("LASTNAME:", rows[2])
    print("AGE:", rows[3])
    print("SALARY:", rows[4])
    print("TASK:", rows[5])
con.close()