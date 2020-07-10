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

#check if record exist in table
def checkCustomerExist(conn, item):
    conn.execute("""
        SELECT *
        FROM customers
        WHERE first_name = '{0}' AND last_name = '{1}'
        """.format(item[0], item[1]))
    if conn.fetchone():
        return True
    return False

#Query the database and return all records
def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers")
    list(map(print, c.fetchall()))
    conn.commit()
    conn.close()

def createEmailTable():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    #Create a table
    if not checkTableExists(c, 'customers'):
        c.execute("""CREATE TABLE customers (
                first_name text,
                last_name text,
                email text
                )"""
        )
    conn.commit()
    conn.close()

def insertCustomers(manyCustomers):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    #Insert multiple values into table
    for item in manyCustomers:
        if not checkCustomerExist(c, item):
            c.execute("INSERT INTO customers VALUES (?,?,?)", item)
    conn.commit()
    conn.close()


#Delete table
#c.execute("DROP TABLE customers")

#Delete Records
#c.execute("DELETE from customers WHERE rowid = 3")

#Update table
#c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = 3 """)

#Query the database
#Query list and format
#for item in c.fetchall(): print(item)