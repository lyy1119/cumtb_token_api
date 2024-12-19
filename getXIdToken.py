import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re

def process_url_to_token(url):
    pattern = r"idToken=(.+?)#/"
    match = re.search(pattern, url)
    return match.group(1) if match else None

async def get_x_id_token(id: str, pwd: str):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver_service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=driver_service, options=options)
    res = {}
    token = ''
    try:
        # 异步执行 Selenium 操作
        loop = asyncio.get_event_loop()
        login_url = 'https://jwxt.cumtb.edu.cn/eams-student-grade-app/index.html'

        await loop.run_in_executor(None, driver.get, login_url)
        username_field = driver.find_element(By.NAME, 'username')
        password_field = driver.find_element(By.ID, 'password')

        username_field.send_keys(id)
        password_field.send_keys(pwd)
        password_field.send_keys(Keys.RETURN)

        url = driver.current_url
        token = process_url_to_token(url)
        res["state"] = 1
    except:
        res["state"] = 0
        res["error"] = "passwordError"
    finally:
        driver.quit()
        res["token"] = token
        return res
