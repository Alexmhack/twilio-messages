import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.getenv("TWILLIO_SID")
account_token = os.getenv("TWILLIO_TOKEN")

twillio_number = os.getenv("TWILLIO_NUMBER")

message_body = "This is a twillio message."

base_url = "https://api.twilio.com/2010-04-01/Accounts"
