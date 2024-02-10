import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config["NEWS_API_KEY"]
country = "pl"
url = "https://newsapi.org/v2/top-headlines"

r = requests.get(f"{url}?country={country}&apiKey={api_key}")
print(r.json())