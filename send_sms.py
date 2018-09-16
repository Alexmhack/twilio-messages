import os
import requests

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

account_sid = os.getenv("TWILLIO_SID")
account_token = os.getenv("TWILLIO_TOKEN")

twillio_number = os.getenv("TWILLIO_NUMBER")
to_number = os.getenv("TO_NUMBER")

message_body = "This is a twillio message."

base_url = "https://api.twilio.com/2010-04-01/Accounts"

auth_cred = (account_sid, account_token)

twillio_url = base_url + '/' + account_sid + '/Messages'

post_data = {
	'From': twillio_number,
	'To': to_number,
	'Body': 'This is a twillio message'
}

res = requests.post(twillio_url, data=post_data, auth=auth_cred)

print(res.status_code)
print(res.text)
