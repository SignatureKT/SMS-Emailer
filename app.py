import database, sys, subprocess, os

commandsHelp = [
    'createtable - Creates a table in the database',
    'add - Creates a record in the table',
    'add+ - Creates mulitple records in the table',
    'delete - Deletes a record in the table',
    'show - Displays records from the table by searching the table\'s columns and name of the search',
    'showall - Displays all records from the table',
    'help - Displays all commands and usage'
    'exit - Exits the application'
]

commands = [
    'createtable',
    'add',
    'add+',
    'delete',
    'show',
    'showall',
    'help',
    'exit'
]

def main():
    #recieve user input to create/open database
    databaseName = getDatabase()
    #if there is no table in the database, the user may create one
    if not database.checkTableExistsDB(databaseName):
        addTableOption(databaseName)
    print("To exit the program enter 'exit':")
    userInput = input().lower().strip()
    while userInput != 'exit':
        if userInput == commands[0]:
            database.createTable(databaseName, getTableNameInput())
        elif userInput == commands[1]:
            database.add_one(databaseName, getTableNameInput(), addOneInput())
        elif userInput == commands[2]:
            database.add_many(databaseName, getTableNameInput(), addMultiple())
        elif userInput == commands[3]:
            database.delete_one(databaseName, getTableNameInput(), deleteOneInput(databaseName))
        elif userInput == commands[4]:
            database.query(databaseName, getTableNameInput(), showInput())
        elif userInput == commands[5]:
            database.show_all(databaseName, getTableNameInput())
        elif userInput == commands[6]:
            lineBreak()
            for string in commandsHelp: print(f'{string}\n')
            lineBreak()
        else:
            print("Invalid Command. Type in 'help' to see list of commands and usage")
        userInput = input().lower().strip()

############################FUNCTIONS##############################################

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
def deleteOneInput(databaseName):
    database.show_all(databaseName, getTableNameInput())
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

#get input for tables
def getTableNameInput():
    print("Which table would you like to look at:")
    return input()

#def get database from user
def getDatabase():
    print("Which database would you like to use (A new database will be created if there is no database under the same name):")
    databaseName = input().lower().strip() + '.db'
    return databaseName

def addTableOption(databaseName):
    print(f'There is no table in {databaseName}. Would you like to create one: [y/n]:')
    if input() == 'y':
        database.createTable(databaseName, getTableNameInput())

def lineBreak():
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
    x = 0
    line = ''
    while x < int(columns):
        line += '='
        x += 1
    print(line)



main()