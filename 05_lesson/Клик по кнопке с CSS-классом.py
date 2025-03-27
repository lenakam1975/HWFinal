from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд.
# Убедитесь, что он отработает одинаково.

driver.get("https://uitestingplayground.com/classattr")
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-primary'))
)
button.click()


sleep(2)
