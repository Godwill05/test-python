import requests

def fetch_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["value"]
    else:
        raise Exception("Erreur lors de la récupération de la blague")

