import re
import requests
user = 'natas1'
password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'
url = 'http://{}.natas.labs.overthewire.org'.format(user)
r = requests.get(url, auth=(user, password)).text
print(re.findall('<!--The password for natas2 is (.*) -->', r)[0])