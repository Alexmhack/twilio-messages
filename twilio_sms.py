import os

from twilio.rest import Client
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.getenv("TWILLIO_SID")
auth_token = os.getenv("TWILLIO_TOKEN")

client = Client(account_sid, auth_token)

twillio_number = os.getenv("TWILLIO_NUMBER")
to_number = os.getenv("TO_NUMBER")

message = client.messages.create(
	from_=twillio_number,
	body='Hello there! Python Programmer',
	to=to_number
)

print(message.sid)
