from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд.
# Убедитесь, что он отработает одинаково.

driver.get('http://uitestingplayground.com/dynamicid')

button = driver.find_element(
    By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"
)
button.click()

sleep(2)
