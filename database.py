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

#Recieves a list of three values records them into the table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

#Add a new record to the table
def add_one(customer):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", customer)
    conn.commit()
    conn.close()

#Recieves a unique ID and delete the record that matches the ID
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", [id])
    conn.commit()
    conn.close()

#Query columns based on user input
def query(item):
    if item[0] == 'rowid':
        queryID(item[1])
    elif item[0] == 'first_name':
        queryFirstName(item[1])
    elif item[0] == 'last_name':
        queryLastName(item[1])
    elif item[0] == 'email':
        queryEmail(item[1])

#Query based on ID
def queryID(value):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE rowid = (?)", [value])
    list(map(print, c.fetchall()))
    conn.close()

#Query based on first_name
def queryFirstName(value):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE first_name = (?)", [value])
    list(map(print, c.fetchall()))
    c.close()

#Query based on last_name
def queryLastName(value):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE last_name = (?)", [value])
    list(map(print, c.fetchall()))
    conn.close()

#Query based on Email
def queryEmail(value):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE email = (?)", [value])
    list(map(print, c.fetchall()))
    c.close()

#Get input from user
def addOneInput():
    print('What is the first name you want to put into the table:')
    firstName = input()
    print('last name:')
    lastName = input()
    print('email:')
    email = input()
    return firstName, lastName, email

#Get input from user
def deleteOneInput():
    show_all()
    print('Which id would you like to delete:')
    return input()

#Creates a list and get multiple input from user
def addMultiple():
    customerDict = []
    userInput = 'y'
    while userInput != 'n':
        if userInput == 'y':
            customerDict.append(addOneInput())
            print(customerDict)
        else:
            print("Invalid Prompt")
        print('Continue?[Y/N]:')
        userInput = input().lower().strip()
    return customerDict

#Get input for columns and value from user
def showInput():
    print('What is the key you like to use to search (rowid, first_name, last_name, or email):')
    key = input()
    print('What is the value you would like to search:')
    value = input()
    return key, value

#Delete table
#c.execute("DROP TABLE customers")

#Delete Records
#c.execute("DELETE from customers WHERE rowid = 3")

#Update table
#c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = 3 """)

#Query the database
#Query list and format
#for item in c.fetchall(): print(item)