import database
import sys

def main():
    #recieve user input to create/open database
    databaseName = getDatabase()
    #if there is no table in the database, the user may create one
    if not database.checkTableExistsDB(databaseName):
        addTableOption(database)
    print("To exit the program enter 'exit'")
    userInput = input().lower().strip()
    while userInput != 'exit':
        if userInput == 'createtable':
            database.createTable(databaseName, getTableNameInput())
        elif userInput == 'add':
            database.add_one(databaseName, getTableNameInput(), addOneInput())
        elif userInput == 'add+':
            database.add_many(databaseName, getTableNameInput(), addMultiple())
        elif userInput == 'delete':
            database.delete_one(databaseName, getTableNameInput(), deleteOneInput(databaseName))
        elif userInput == 'show':
            database.query(databaseName, getTableNameInput(), showInput())
        elif userInput == 'showall':
            database.show_all(databaseName, getTableNameInput())
        elif userInput == 'help':
            print("The commands are 'exit', 'add', 'add+', 'showall', 'show', and 'delete', 'createtable'")
        else:
            print("Invalid Command. Type in 'help' to see list of commands")
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
main()