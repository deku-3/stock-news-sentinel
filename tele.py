import os
import requests
from dotenv import load_dotenv
load_dotenv()

def send_telegram_message(message):

    TELEGRAM_BOT_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHAT_ID=os.getenv(TELEGRAM_CHAT_ID)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"

    }
    try:
        response = requests.post(url, data=payload)
        if not response.ok:
            print("❌ Failed to send Telegram message:", response.text)
    except Exception as e:
        print("❌ Error sending Telegram message:", e)

