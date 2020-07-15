import database, sys, subprocess, os, user
commandsHelp = [
    'createtable - Creates a table in the database',
    'add - Creates a record in the table',
    'add+ - Creates mulitple records in the table',
    'delete - Deletes a record in the table',
    'show - Displays records from the table by searching the table\'s columns and name of the search',
    'showall - Displays all records from the table',
    'mail - mails to the people in the tables',
    'showtables - show all tables in the current database',
    'deletetable - delete table from the database',
    'changedb - changes current database to a new database',
    'removedb - removes specified database',
    'update - updates a record on the table',
    'help - Displays all commands and usage',
    'exit - Exits the application'
]

commands = [
    'createtable',
    'add',
    'add+',
    'delete',
    'show',
    'showall',
    'mail',
    'showtables',
    'deletetable',
    'changedb',
    'removedb',
    'update',
    'help',
    'exit'
]

#recieve user input to create/open database
databaseName = user.getDatabase()
#if there is no table in the database, the user may create one
if not database.checkTableExistsDB(databaseName):
    if user.addTableOption(databaseName) == True:
        database.createTable(databaseName, user.getTableNameInput())
print("To exit the program enter 'exit':")
userInput = input('menu: ').lower().strip()
while userInput != 'exit':
    if userInput == commands[0]:
        database.createTable(databaseName, user.getTableNameInput())
    elif userInput == commands[1]:
        database.add_one(databaseName, user.getTableNameInput(), user.addOneInput())
    elif userInput == commands[2]:
        database.add_many(databaseName, user.getTableNameInput(), user.addMultiple())
    elif userInput == commands[3]:
        tableName = user.getTableNameInput()
        database.show_all(databaseName, tableName)
        database.delete_one(databaseName, tableName, user.deleteOneInput(databaseName, tableName))
    elif userInput == commands[4]:
        database.query(databaseName, user.getTableNameInput(), user.showInput())
    elif userInput == commands[5]:
        database.show_all(databaseName, user.getTableNameInput())
    elif userInput == commands[6]:
        subprocess.run([sys.executable, f"./mails.py", f'{databaseName}', f'{user.getTableNameInput()}'])
    elif userInput == commands[7]:
        database.showTables(databaseName)
    elif userInput == commands[8]:
        database.deleteTable(databaseName, user.getTableNameInput())
    elif userInput == commands[9]:
        databaseName = user.getNewDatabaseInput()
    elif userInput == commands[10]:
        user.deleteDatabaseInput()
    elif userInput == commands[11]:
        database.updateTable(databaseName, user.getTableNameInput(), user.updateInput())
    elif userInput == commands[12]:
        user.lineBreak()
        for string in commandsHelp: print(f'{string}\n')
        user.lineBreak()
    else:
        print("Invalid Command. Type in 'help' to see list of commands and usage")
    userInput = input('menu: ').lower().strip()