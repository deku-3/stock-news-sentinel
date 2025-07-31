import requests


def send_telegram_message(message):
    TELEGRAM_BOT_TOKEN = "7764932403:AAHMiZSI33jgTglCn6k80da804sjdPDLBSs" 
    TELEGRAM_CHAT_ID = 1065095420  
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

