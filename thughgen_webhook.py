import string, random
from flask import Flask, request
import requests

BOT_TOKEN = ""
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

def generate_password(length=12, use_digits=True, use_punct=True, use_upper=True, use_lower=True):
    pools = []
    if use_lower: pools.append(string.ascii_lowercase)
    if use_upper: pools.append(string.ascii_uppercase)
    if use_digits: pools.append(string.digits)
    if use_punct: pools.append("!@#$%^&*()-_=+[]{};:,.<>/?")
    if not pools:
        pools = [string.ascii_letters + string.digits]
    password_chars = [random.choice(pool) for pool in pools]
    all_chars = ''.join(pools)
    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))
    random.shuffle(password_chars)
    return ''.join(password_chars[:length])

def send_message(chat_id, text, reply_to=None):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"  # فعال بودن Markdown
    }
    if reply_to:
        data["reply_to_message_id"] = reply_to
    requests.post(f"{API_URL}/sendMessage", json=data)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json(force=True)
    if "message" in update:
        msg = update["message"]
        text = msg.get("text", "")
        chat_id = msg["chat"]["id"]
        msg_id = msg.get("message_id")

        if text.startswith("/start"):
            send_message(chat_id,
                "*سلام!* 👋\n"
                "من ربات تولید پسورد هستم، اسمم *ThughGen* هست.\n\n"
                "برای شروع از دستور زیر استفاده کن:\n"
                "👉 `/generate 12`\n\n"
                "_برای دیدن همه دستورات از_ /help استفاده کن.",
                reply_to=msg_id
            )

        elif text.startswith("/help"):
            send_message(chat_id,
                "📖 *راهنمای دستورات:*\n\n"
                "🔑 `/generate <length>`\n"
                "➡️ تولید پسورد پیچیده با طول مشخص.\n\n"
                "🔐 `/generate_safe <length>`\n"
                "➡️ تولید پسورد فقط شامل حروف و اعداد.\n\n"
                "_مثال:_ `/generate 16`",
                reply_to=msg_id
            )

        elif text.startswith("/generate_safe"):
            try:
                length = int(text.split()[1]) if len(text.split()) > 1 else 12
            except:
                length = 12
            length = max(4, min(128, length))
            pwd = generate_password(length, use_digits=True, use_punct=False, use_upper=True, use_lower=True)
            send_message(chat_id,
                f"🔐 *پسورد امن {length} کاراکتری:*\n\n"
                f"`{pwd}`\n\n"
                "_یادت باشه این پیام در چت ذخیره میشه!_", 
                reply_to=msg_id
            )

        elif text.startswith("/generate"):
            try:
                length = int(text.split()[1]) if len(text.split()) > 1 else 12
            except:
                length = 12
            length = max(4, min(128, length))
            pwd = generate_password(length, use_digits=True, use_punct=True, use_upper=True, use_lower=True)
            send_message(chat_id,
                f"🔑 *پسورد {length} کاراکتری ساخته شد:*\n\n"
                f"`{pwd}`\n\n"
                "_مراقب باش، پیام رو جایی ذخیره نکن!_", 
                reply_to=msg_id
            )

        else:
            send_message(chat_id,
                "❌ *دستور ناشناخته!*\n"
                "برای لیست کامل دستورات از /help استفاده کن.", 
                reply_to=msg_id
            )

    return {"ok": True}
