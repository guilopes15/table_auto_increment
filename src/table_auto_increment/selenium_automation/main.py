import platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .automation_procedure import send_data

chrome_options = Options()
chrome_options.add_argument('--log-level=3')

if 'wsl' in platform.uname().release.lower():
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(1)

driver.get('http://localhost:8000')

data = [['t', 1, 'apenas'], ['e', 2, 'um'], ['s', 3, 'test']]

for items in data:
    send_data(driver, items)

driver.quit()
