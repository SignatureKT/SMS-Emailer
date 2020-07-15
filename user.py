import subprocess, os

#Get input from user
def addOneInput():
    print('What is the first name you want to put into the table:')
    firstName = input('first name: ')
    lastName = input('last name: ')
    email = input('email: ')
    phone = input('phone: ')
    return firstName, lastName, email, phone

#Get input from user
def deleteOneInput(databaseName, tableName):
    print('Which record would you like to delete:')
    return input('rowid: ')

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
    print('What is the key you like to use to search\n(rowid, first_name, last_name, email, or phone):')
    key = input()
    print('What is the value you would like to search:')
    value = input()
    return key, value

def updateInput():
    print('What is the key you like to use to search\n(rowid, first_name, last_name, email, or phone):')
    key = input()
    print('What rowid you would like to use to update you record:')
    rowid = input('rowid:')
    print('What would you like to change the value to:')
    value = input('value: ')
    return key, value, rowid

#get input for tables
def getTableNameInput():
    print("Which table would you like to look/create at:")
    return input('table: ')

#def get database from user
def getDatabase():
    print("Which database would you like to use\n(A new database will be created if there is no database under the same name):")
    databaseName = input('database: ').lower().strip() + '.db'
    return databaseName

def addTableOption(databaseName):
    print(f'There is no table in {databaseName}. Would you like to create one: [y/n]:')
    if input() == 'y':
        return True
    else:
        return False

def lineBreak():
    _, columns = subprocess.check_output(['stty', 'size']).decode().split()
    line = ''
    for _ in range(len(columns)):
        line += '='
    print(f'{line}\n')

def getNewDatabaseInput():
    print('Which database would you like to switch to:')
    databaseName = input('database: ').lower().strip() + '.db'
    return databaseName

def deleteDatabaseInput():
    print('Which database would you like to switch to:')
    databaseName = input('database:')
    print(f'Delete {databaseName}? [y/n]')
    userInput = input()
    while userInput != 'n':
        if userInput == 'y':
            os.remove(databaseName)
            return 0
        print(f'Invalid Input. Delete {databaseName}? [y/n]')
        userInput = input()