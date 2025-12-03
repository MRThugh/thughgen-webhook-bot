
````markdown
# ThughGen Webhook Bot

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&logoColor=white)](https://telegram.org/)

ThughGen is a **Telegram bot** powered by **Webhooks**, designed to generate strong, customizable, and secure passwords instantly.

---

## ⚡ Features
- Generate complex passwords with `/generate <length>`
- Generate safe alphanumeric passwords with `/generate_safe <length>`
- Lightweight and fast — no polling needed, uses Webhook for real-time updates
- Fully open-source and easy to customize
- Markdown messages support

---

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/MRThugh/thughgen-webhook-bot.git
cd thughgen-webhook-bot
````

2. Install dependencies:

```bash
pip install flask requests
```

3. Set your Telegram bot token in `bot.py`:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

4. Set up your HTTPS server endpoint for Webhook:

```
https://yourdomain.com/YOUR_BOT_TOKEN
```

5. Register the webhook with Telegram API:

```bash
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://yourdomain.com/<YOUR_BOT_TOKEN>
```

6. Run the bot:

```bash
python bot.py
```

> 💡 For Python beginners:  
> Instead of installing packages individually, you can install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt


---

## 📝 Commands

| Command                   | Description                                            |
| ------------------------- | ------------------------------------------------------ |
| `/start`                  | Introduction and basic instructions                    |
| `/help`                   | Show all available commands                            |
| `/generate <length>`      | Generate a complex password (default length: 12)       |
| `/generate_safe <length>` | Generate a safe password with letters and numbers only |

---

## ⚙️ Customization

* Modify `generate_password()` function to change password rules
* Update messages in `send_message()` function
* Add new commands by editing the `webhook()` function

---

## 🔒 Notes

* `/generate` includes symbols for high-security passwords
* `/generate_safe` avoids symbols for easier typing
* All passwords are sent as Markdown messages

---

## 📝 License

MIT License

