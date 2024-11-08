from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re

def process_url_to_token(url):
    # 正则表达式：匹配开头 idToken=，并提取中间内容，直到 #/
    pattern = r"idToken=(.+?)#/"

    match = re.search(pattern, url)
    if match:
        content = match.group(1)
        return content
    else:
        return None


def get_x_id_token(id: str , pwd: str):
    # 设置 WebDriver（以 Chrome 为例）
    # driver = webdriver.Chrome()
    options = Options()
    options.add_argument("--headless")  # 无头模式
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    # 打开登录页面
    login_url = 'https://jwxt.cumtb.edu.cn/eams-student-grade-app/index.html'
    driver.get(login_url)
    # 查找并填写用户名和密码
    username_field = driver.find_element(By.NAME, 'username')
    password_field = driver.find_element(By.ID, 'password')
    username_field.send_keys(id)
    password_field.send_keys(pwd)
    # 提交表单
    password_field.send_keys(Keys.RETURN)
    # 获取登录后的页面内容
    url = driver.current_url
    # 关闭浏览器
    driver.quit()
    return process_url_to_token(url)