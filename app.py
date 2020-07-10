import database

manyCustomers = [
    ('Kevin', 'Truong', 'KevinTruong@example.com'),
    ('Mary', 'Jane', 'MaryJane@example.com'),
    ('Bob', 'By', 'Bobby@example.com'),
    ('Daniel', 'Snow', 'DanielSnow@example.com'),
    ('Joe', 'Baker', 'JoeBaker@example.com'),
    ('Tom', 'Rain', 'TomRain@exmaple.com'),
    ('Pat', 'Fried','PatFried@example.com')
    ]
database.insertCustomers(manyCustomers)
database.show_all()