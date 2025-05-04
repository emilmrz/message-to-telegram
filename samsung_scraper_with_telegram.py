from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# Telegram məlumatları
bot_token = '8083036642:AAEbjPT5u1iFVW4BFsRmYTyhBiiCnRthtWk'
chat_id = '5798795140'

# Selenium başlat
options = Options()
options.add_argument("--start-maximized")  # Headless silindi ki, brauzer görünsün
# options.add_argument("--headless")  # Əgər istəsən sonradan əlavə edə bilərsən

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Sayta keçid
    url = "https://kontakt.az/az/smartfonlar/filter/istehsalci=samsung/model=samsung-galaxy-s21,samsung-galaxy-s21-plus,samsung-galaxy-s21-ultra,samsung-galaxy-s22,samsung-galaxy-s22-plus,samsung-galaxy-s22-ultra,samsung-galaxy-s23,samsung-galaxy-s23-plus,samsung-galaxy-s23-ultra,samsung-galaxy-s24,samsung-galaxy-s24-plus,samsung-galaxy-s24-ultra"
    driver.get(url)

    # Bir az gözlə ki, səhifə yüklənsin
    time.sleep(5)

    # Model və qiymətləri tap
    models = driver.find_elements(By.CLASS_NAME, "product-name")
    prices = driver.find_elements(By.CLASS_NAME, "product-price-value")

    if models and prices:
        message = "Samsung modelləri və qiymətləri:\n\n"
        for model, price in zip(models, prices):
            model_text = model.text.strip()
            price_text = price.text.strip()
            message += f"📱 {model_text} - {price_text}\n"
        print(message)
    else:
        message = "Model və ya qiymətlər tapılmadı."
        print(message)

    # Telegrama göndər
    send_text = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(send_text)

    if response.status_code == 200:
        print("Telegram mesajı göndərildi ✅")
    else:
        print("Telegram mesaj göndərilə bilmədi ❌")
        print("Kod:", response.status_code, response.text)

except Exception as e:
    print("Xəta baş verdi:", e)

finally:
    driver.quit()
