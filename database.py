import sqlite3

#create a connection
conn = sqlite3.connect('customer.db')

#Create a cursor
c = conn.cursor()

#Create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text) """
)

#Commit our command
conn.commit()

#Commit our connection
conn.close()
