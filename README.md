# Twillio-Messages
tinkering with [Twillio](http://twillio.com) services using python

Go to [Twillio](https://www.twilio.com/login) and create a new account or simply login if you already have an 
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


