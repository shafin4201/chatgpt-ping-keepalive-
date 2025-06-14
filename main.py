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

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://chat.openai.com")

    # Load cookies
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()
    print("✅ ChatGPT pinged successfully.")
    driver.quit()

# Run every 7 minutes
schedule.every(7).minutes.do(ping)
ping()  # First run immediately
while True:
    schedule.run_pending()
    time.sleep(1)