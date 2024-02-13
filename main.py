import requests
import schedule
import time
from dotenv import dotenv_values

import mail_sender

env = dotenv_values(".env")
api_key = env["NEWS_API_KEY"]
country = "pl"
category = "technology"
page_size = 5
url = "https://newsapi.org/v2/top-headlines"

print("Program was started, You receive an email at schedule time")


def job():
    r = requests.get(f"{url}?country={country}&category={category}&pageSize={page_size}&apiKey={api_key}")

    message = mail_sender.set_email_content(r.json()['articles'])
    message = message.encode("utf-8")
    mail_sender.send_email(message)


schedule.every().day.at('08:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
