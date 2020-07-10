import sqlite3

#check if table exist
def checkTableExists(conn, tablename):
    conn.execute("""
        SELECT count(name)
        FROM sqlite_master
        WHERE type='table' AND name = '{0}'
        """.format(tablename))
    if conn.fetchone()[0] == 1:
        return True
    return False

#create a connection
conn = sqlite3.connect('customer.db')

#Create a cursor
c = conn.cursor()

#Create a table
if not checkTableExists(c, 'customers'):
    c.execute("""CREATE TABLE customers (
            first_name text,
            last_name text,
            email text
            )"""
    )

#Delete Records
#c.execute("Delete from customers WHERE rowid = 3")

#Update table
#c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = 3 """)

#Query the database - ORDER BY
c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
#list(map(print, c.fetchall()))
#Query list and format
for item in c.fetchall(): print(item)

#manyCustomers = [
#    ('Mary', 'Jane', 'MaryJane@example.com'),
#    ('Bob', 'By', 'Bobby@example.com'),
#    ('Daniel', 'Snow', 'DanielSnow@example.com')
#    ]

#Insert multiple values into table
#c.executemany("INSERT INTO customers VALUES (?,?,?)", manyCustomers)

#Commit our command
conn.commit()

#Commit our connection
conn.close()
