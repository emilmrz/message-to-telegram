---

## Samsung Price Scraper with Telegram Notifications 📱💬

This Python script scrapes Samsung Galaxy S21 and newer models from **Kontakt.az** and sends the extracted model names and prices directly to a Telegram chat using a bot.

---

### 🔹 Features

* Scrapes Samsung Galaxy S21, S22, S23, S24 series models from Kontakt.az.
* Extracts product names and prices.
* Sends the results to a Telegram chat.
* Uses **Selenium** (works with dynamic content).
* Sends real-time notifications through **Telegram Bot API**.

---

### 🔹 Requirements

You need to have:

* Python 3.8 or newer
* Google Chrome browser
* ChromeDriver

Python libraries (install with pip):

```
pip install selenium
pip install webdriver_manager
pip install requests
```

---

### 🔹 How the Script Works

1. Opens Kontakt.az with Samsung models filter.
2. Extracts phone model names and their prices.
3. Prepares a message with the data.
4. Sends the message to your Telegram chat.

---

### 🔹 How to Get a Telegram Bot Token & Chat ID

**Step 1:**
Go to Telegram and search **@BotFather**. Create a new bot and get the token.

**Step 2:**
Send a message (like "Hello") to your bot to activate the chat.

**Step 3:**
Open this URL (replace YOUR\_BOT\_TOKEN):

```
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```

**Step 4:**
Look for `"chat":{"id":...}` in the result — that number is your **chat ID**.

---

### 🔹 How to Use

1. In the script, change these lines:

```python
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'
```

2. Save and run the script:

```
python samsung_scraper_with_telegram.py
```

3. The script will scrape the data and send it to your Telegram chat.

---

### 🔹 Example Output in Telegram

```
Samsung modelləri və qiymətləri:

📱 Samsung Galaxy S24 Ultra - 2999 AZN
📱 Samsung Galaxy S23 - 1999 AZN
📱 Samsung Galaxy S22 Plus - 1599 AZN
```

---

### 🔹 Notes

* If the website changes, the scraper may need updates.
* If you get `403 Forbidden` or no data, the website might be blocking bots — but Selenium usually bypasses this.
* If no models or prices are found, you’ll see a message and no Telegram message will be sent.

---

### 🔹 License

For educational purposes only. Make sure to follow the website’s scraping policy.

---

**Happy scraping and automating! 😎🤖**

---

