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

def checkCustomerExist(conn, item):
    conn.execute("""
        SELECT *
        FROM customers
        WHERE first_name = '{0}' AND last_name = '{1}'
        """.format(item[0], item[1]))
    if conn.fetchone():
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

#Delete table
#c.execute("DROP TABLE customers")

#Delete Records
#c.execute("DELETE from customers WHERE rowid = 3")

#Update table
#c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = 3 """)

manyCustomers = [
    ('Kevin', 'Truong', 'KevinTruong@example.com'),
    ('Mary', 'Jane', 'MaryJane@example.com'),
    ('Bob', 'By', 'Bobby@example.com'),
    ('Daniel', 'Snow', 'DanielSnow@example.com'),
    ('Joe', 'Baker', 'JoeBaker@example.com'),
    ('Tom', 'Rain', 'TomRain@exmaple.com'),
    ('Pat', 'Fried','PatFried@example.com')
    ]

#Insert multiple values into table
for item in manyCustomers:
    if not checkCustomerExist(c, item):
        c.execute("INSERT INTO customers VALUES (?,?,?)", item)


#Query the database - ORDER BY
c.execute("SELECT rowid, * FROM customers")
list(map(print, c.fetchall()))
#Query list and format
#for item in c.fetchall(): print(item)
#Commit our command
conn.commit()

#Commit our connection
conn.close()