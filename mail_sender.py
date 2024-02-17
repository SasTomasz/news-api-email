import smtplib
import ssl
from dotenv import dotenv_values

import logger_utils

logger = logger_utils.logger


def send_email(msg_content=None):
    env = dotenv_values(".env")

    host = 'smtp.gmail.com'
    port = 587
    password = env["SENDER_PASSWORD"]
    email_sender = env["SENDER_LOGIN"]
    email_receiver = env["EMAIL_RECEIVER"]
    if msg_content:
        message = msg_content
    else:
        message = """\
Subject: Technology news
This is a message from news-api-email
"""

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(host, port)
        server.starttls(context=context)
        server.login(email_sender, password)
        server.sendmail(email_sender, email_receiver, message)
        server.quit()
        logger.info("Email was sent successfully")
        return True
    except Exception as e:
        logger.error(e)
        return False


def set_email_content(news: dict = None):
    message = f"""\
Subject: Technology news"""

    if news:
        for article in news:
            message = message + '\n' + "Tytuł: " + article['title']
            message = message + '\n' + "Url: " + article['url'] + "\n"
        return message


if __name__ == "__main__":
    send_email()
