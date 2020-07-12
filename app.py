import database
import sys

print("To exit the program enter 'exit':")
userInput = input().lower().strip()
while userInput != 'exit':
    if userInput == 'add':
        database.add_one(database.addOneInput())
    elif userInput == 'add+':
        database.add_many(database.addMultiple())
    elif userInput == 'delete':
        database.delete_one(database.deleteOneInput())
    elif userInput == 'show':
        database.query(database.showInput())
    elif userInput == 'showall':
        database.show_all()
    elif userInput == 'help':
        print("The commands are 'exit', 'add', 'add+', 'showall', 'show', and 'delete'")
    else:
        print("Invalid Command. Type in 'help' to see list of commands")
    userInput = input().lower().strip()