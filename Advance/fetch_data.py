from urllib.request import urlopen
import json


def fetch_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


url = "http://official-joke-api.appspot.com/jokes/programming/random"
data = fetch_data(url)
print(data)
