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

#check if table exists in database
def checkTableExistsDB(databaseName):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"""
        SELECT count(name)
        FROM sqlite_master
        WHERE type='table'
    """)
    if c.fetchone()[0] == 1:
        c.close()
        return True
    c.close()
    return False
#check if record exist in table
def checkCustomerExist(conn, tableName, item):
    conn.execute(f"""
        SELECT *
        FROM tableName
        WHERE first_name = '{item[0]}' AND last_name = '{item[1]}'
        """)
    if conn.fetchone():
        return True
    return False

#Query the database and return all records
def show_all(databaseName, tableName):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM {tableName}")
    list(map(print, c.fetchall()))
    conn.close()

def createTable(databaseName, tableName):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    #Create a table
    if not checkTableExists(c, f'{tableName}'):
        c.execute(f"""CREATE TABLE {tableName} (
                first_name text,
                last_name text,
                email text
                )"""
        )
    conn.commit()
    conn.close()

#Recieves a list of three values records them into the table
def add_many(databaseName, tableName,list):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.executemany(f"INSERT INTO {tableName} VALUES {list}")
    conn.commit()
    conn.close()

#Add a new record to the table
def add_one(databaseName, tableName, item):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"INSERT INTO {tableName} VALUES {item}")
    conn.commit()
    conn.close()

#Recieves a unique ID and delete the record that matches the ID
def delete_one(databaseName, tableName, id):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"DELETE from {tableName} WHERE rowid = {id}")
    conn.commit()
    conn.close()

#Query columns based on user input
def query(databaseName, tableName, item):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"SELECT rowid, * FROM {tableName} WHERE {item[0]} = '{item[1]}'")
    list(map(print, c.fetchall()))
    c.close()

def showTables(databaseName):
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"SELECT name FROM sqlite_master WHERE type='table'")
    print(f'{databaseName} tables: ')
    list(map(print, c.fetchall()))
    c.close()

def deleteTable(databaseName, tableName):
    conn = sqlite3.connect()
    c = conn.cursor()
    c.execute(f"DROP TABLE {tableName}")
    c.close()

#Update table
#c.execute("""UPDATE customers SET first_name = 'Bob' WHERE rowid = 3 """)