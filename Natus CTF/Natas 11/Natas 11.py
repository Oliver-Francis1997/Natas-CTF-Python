import re
import requests
import html

user = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = 'http://{}.natas.labs.overthewire.org/'.format(user)
#data = {'needle' : '. /etc/natas_webpass/natas11 #', 'submit' : 'Search'}
r = requests.Session().post(url + 'index-source.html', auth=(user, password)).text
print(html.unescape(r))
#print(re.findall('pre>\n(.*)', r)[0])