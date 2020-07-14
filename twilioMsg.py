from twilio.rest import Client
import os
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
TO_NUMBER = os.environ.get("MY_PHONE_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

phoneNumbers = [TO_NUMBER]

index = 0
while index < len(phoneNumbers):
    client.messages.create(
        to=phoneNumbers[index],
        from_=FROM_NUMBER,
        body="HELLO WORLD"
        )
    index += 1