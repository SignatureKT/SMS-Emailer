import database
import sys

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

exmapleCustomers = [
    ('Jose', 'Moris', 'JoseMoris@example.com'),
    ('Sara', 'Wills', 'SaraWills@example.com'),
    ('June', 'Renning', 'JuneRenning@example.com')
]

#database.add_one(addOneInput())
database.add_many(exmapleCustomers)
#database.delete_one(deleteOneInput())
database.show_all()