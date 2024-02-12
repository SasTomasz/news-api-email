import requests
from dotenv import dotenv_values
import mail_sender

env = dotenv_values(".env")
api_key = env["NEWS_API_KEY"]
country = "pl"
category = "technology"
page_size = 5
url = "https://newsapi.org/v2/top-headlines"

r = requests.get(f"{url}?country={country}&category={category}&pageSize={page_size}&apiKey={api_key}")

message = mail_sender.set_email_content(r.json()['articles'])
message = message.encode("utf-8")
mail_sender.send_email(message)
# TODO:
#  * Add Timer (see example:
#  https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day)
