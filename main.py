from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import schedule, time, json

def ping():
    print(">> Pinging ChatGPT...")

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # First load the domain so we can add cookies
    driver.get("https://chat.openai.com")

    # Load and set cookies
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        # Selenium requires 'domain' key to be absent when setting cookies
        cookie.pop("sameSite", None)
        cookie.pop("priority", None)
        if "domain" in cookie:
            cookie["domain"] = ".chat.openai.com"
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"❌ Error adding cookie: {e}")

    driver.get("https://chat.openai.com")  # Reload after adding cookies

    print("✅ ChatGPT pinged successfully.")
    driver.quit()

# Schedule the ping
schedule.every(7).minutes.do(ping)

# Initial run
ping()

while True:
    schedule.run_pending()
    time.sleep(1)