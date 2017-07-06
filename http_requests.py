import requests
from requests.exceptions import ConnectionError

def chceck_internet_connection():
    url = "http://www.google.com"

    try:
        response = requests.get(url=url)

        if response.status_code == 200:
            return True
    except:
        return False


print(chceck_internet_connection())