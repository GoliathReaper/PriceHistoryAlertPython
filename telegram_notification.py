import time
import requests
import logging
from dotenv import load_dotenv
import os

env = load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def telegram_message(msg):
    telgram_token = os.getenv("telegram_token")
    chat_id = os.getenv("telegram_chat_id")
    send_msg = f'https://api.telegram.org/bot{telgram_token}/sendMessage?chat_id={chat_id}&text={msg}'
    requests.get(send_msg)
    time.sleep(3)
