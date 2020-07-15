from twilio.rest import Client
import os, sys, sqlite3

def main(databaseName, tableName):
    ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID") if os.environ.get("TWILIO_ACCOUNT_SID") else ''
    AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN") if os.environ.get("TWILIO_AUTH_TOKEN") else ''
    FROM_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER") if os.environ.get("TWILIO_PHONE_NUMBER") else ''
    #TO_NUMBER = os.environ.get("MY_PHONE_NUMBER") if os.environ.get("MY_PHONE_NUMBER") else ''

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    conn = sqlite3.connect(databaseName)
    c = conn.cursor()
    c.execute(f"SELECT count(*) FROM {tableName}")
    length = len(c.fetchall())
    for index in range(length):
        c.execute(f"SELECT * FROM {tableName} WHERE rowid = {index+1}")
        phone = c.fetchone()[3]
        client.messages.create(
            to=phone,
            from_=FROM_NUMBER,
            body="HELLO WORLD"
            )
    conn.close()
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])