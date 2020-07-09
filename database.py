import sqlite3

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
            email text) """
    )

#Commit our command
conn.commit()

#Commit our connection
conn.close()
