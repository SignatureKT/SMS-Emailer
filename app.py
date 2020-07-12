import database


def addOneInput():
    print('What is the first name you want to put into the table:')
    firstName = input()
    print('last name:')
    lastName = input()
    print('email:')
    email = input()
    return firstName, lastName, email

def deleteOneInput():
    database.show_all()
    print('Which id would you like to delete:')
    return input()

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

def showInput():
    print('What is the key you like to use to search (rowid, first_name, last_name, or email):')
    key = input()
    print('What is the value you would like to search:')
    value = input()
    return key, value

exmapleCustomers = [
    ('Jose', 'Moris', 'JoseMoris@example.com'),
    ('Sara', 'Wills', 'SaraWills@example.com'),
    ('June', 'Renning', 'JuneRenning@example.com')
]

print("To exit the program enter 'exit':")
userInput = input().lower().strip()
while userInput != 'exit':
    if userInput == 'add':
        database.add_one(addOneInput())
    elif userInput == 'add+':
        database.add_many(addMultiple())
    elif userInput == 'delete':
        database.delete_one(deleteOneInput())
    elif userInput == 'show':
        database.query(showInput())
    elif userInput == 'showall':
        database.show_all()
    elif userInput == 'help':
        print("The commands are 'exit', 'add', 'add+', 'showall', 'show', and 'delete'")
    else:
        print("Invalid Command. Type in 'help' to see list of commands")
    userInput = input().lower().strip()