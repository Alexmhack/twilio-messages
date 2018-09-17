# Twilio-Messages
tinkering with [twilio](http://twilio.com) services using python

Go to [Twilio](https://www.twilio.com/login) and create a new account or simply login if you already have an 
account. Create project by selecting products like Programmable Chat or any other that 
you want.

Once done you will be redirected to project dashboard and you will get many options for 
sending messages. You can also click onto DOCS on navbar.

Now let's start requesting using python

# Setting Up Environment
Create a ```.env``` file in the project folder. Fill the file with your credentials like

```
TWILLIO_NUMBER=<your-number>
TWILLIO_SID=<your-account-sid>
TWILLIO_TOKEN=<your-account-token>
```

Then if you don't have [dotenv](https://pypi.org/project/python-dotenv/). There are many 
many other packages for handling environment variables from ```.env``` but I would be 
using **dotenv**. 

Using **dotenv** is very simple.

1. Install dotenv

	```
	pip install python-dotenv
	```

2. Import functions from dotenv

	```
	from dotenv import load_dotenv, find_dotenv
	```

3. Call the functions for loading variables from ```.env``` file

	```
	load_dotenv(find_dotenv())
	```

4. Create ```.env``` file with your credentials

	```
	SECRET_KEY=1234567890
	```

5. Access **env** variables using

	```
	import os
	SECRET_KEY = os.getenv("SECRET_KEY")
	```

6. Check if values is correct

	```
	print(SECRET_KEY)
	```

Now writing some python code.

**send_sms.py**
```
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

twillio_number = os.getenv("TWILLIO_NUMBER")

message_body = "This is a twillio message."

base_url = "https://api.twilio.com/2010-04-01/Accounts"
```

```message_body``` can have any string message that you wish.

If you look at the Twilio Docs for sending sms and mms messages. Twilio API requires us to 
send a few values and there are many more values that are optional.

**send_sms.py**
```
...
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
```

**Requests** python module has very powerful features like the ```auth``` and ```data``` 
arguments. Twilio requires Twilio Account SID and Twilio Account Token both so we pass in the
tuple of both. Since we are making a ```post``` request we need to send some data along with 
request. 

We send a **dictionary** with **key value** pairs of data that twilio needs. We send the 
```From``` keyword, ```To``` and ```Body``` with the respective data.

If you print the ```status_code``` of the request you will get ```200``` if the credentials
and data was correct. On printing the ```text``` of the response we get ```xml``` data with
some information of our message and request.

**NOTE:** Before sending the message to a phone number you have to verify that phone number
in twilio. If you send the message to that phone number with which you registered in twilio 
then the message will be sent. Twilio won't send messages to a non-verified phone number.

You will get a error message in ```res.text``` if error occurs.

Alternatively you can use the [twilio](https://www.twilio.com/docs/libraries/python) python
helper library and also use the docs to see how the package works.

Using twilio python library is lot more easier than using requests but we wanted to learn
the advanced features of python requests.

Check the ```twilio_sms.py``` file for sending sms using twilio library.
