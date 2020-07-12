from email.message import EmailMessage
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('MAIL_TEST')
EMAIL_PASSWORD = os.environ.get('PASSWORD_TEST')


contacts = [EMAIL_ADDRESS]

#Creates message and gets contacts
msg = EmailMessage()
msg['Subject'] = ''
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('')

#sends the message 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)