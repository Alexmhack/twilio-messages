import os
import requests

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.getenv("TWILLIO_SID")
account_token = os.getenv("TWILLIO_TOKEN")

twillio_number = os.getenv("TWILLIO_NUMBER")

message_body = "This is a twillio message."

base_url = "https://api.twilio.com/2010-04-01/Accounts"

auth = (account_sid, account_token)

res = requests.get(base_url, auth=auth)

print(res.status_code)
print(res.text)
