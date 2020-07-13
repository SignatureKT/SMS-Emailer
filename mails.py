from email.message import EmailMessage
import os, smtplib, sys, sqlite3

def main(databaseName, tableName):
    EMAIL_ADDRESS = os.environ.get('MAIL_TEST')
    EMAIL_PASSWORD = os.environ.get('PASSWORD_TEST')

    fileDir = './emailFile'

    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"SELECT count(*) FROM {tableName}")
    length = len(c.fetchall())
    index = 1
    while index <= (length + 1):
        c.execute(f"SELECT * FROM {tableName} WHERE rowid = {index}")
        firstName = c.fetchone()[0]
        c.execute(f"SELECT * FROM {tableName} WHERE rowid = {index}")
        lastName = c.fetchone()[1]
        c.execute(f"SELECT * FROM {tableName} WHERE rowid = {index}")
        email = c.fetchone()[2]
        with open(f'{fileDir}/subject.txt', 'w+') as f:
            f.write("Hello, This is a subject!")

        with open(f'{fileDir}/body.txt', 'w+') as f:
            f.write(f"""{firstName} {lastName},\nThis is a test email to be sent to {email}.
            """)

        #Creates message and gets contacts
        msg = EmailMessage()
        with open(f'{fileDir}/subject.txt', 'r') as f:
            msg['Subject'] = f.read()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        with open(f'{fileDir}/body.txt', 'r') as f:
            msg.set_content(f.read())

        #sends the message 
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        index += 1

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])