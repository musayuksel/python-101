# installation: pip3 install requests
# Description: This script will fetch the data from the url and print the data
# https://pypi.org/project/requests/
# https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request

import requests


def fetch_data(url):
    # fetch json data from url and return the data as a dictionary
    response = requests.get(url)
    print(response.status_code)
    return response.json()


url = "https://official-joke-api.appspot.com/random_ten"
data = fetch_data(url)
# print(data)
# print(data[0]["setup"])
# print(data[0]["punchline"])
for joke in data:
    print(f"Q: {joke['setup']}\nA: {joke['punchline']}")
    print()
