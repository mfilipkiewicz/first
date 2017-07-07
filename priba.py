import requests

r = requests.get('https://www.wp.pl', verify = False)
print(r.text)