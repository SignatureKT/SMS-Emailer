import database

print('What is the first name you want to put into the table:')
firstName = input()
print('last name:')
lastName = input()
print('email:')
email = input()
database.add_one(firstName, lastName, email)
database.show_all()