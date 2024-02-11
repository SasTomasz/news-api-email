import requests
from dotenv import dotenv_values

def create_mail_content(content: dict = None):
    content_header = f""


config = dotenv_values(".env")
api_key = config["NEWS_API_KEY"]
country = "pl"
category = "technology"
url = "https://newsapi.org/v2/top-headlines"

r = requests.get(f"{url}?country={country}&category={category}&apiKey={api_key}")
for article in r.json()['articles']:
    print(article)