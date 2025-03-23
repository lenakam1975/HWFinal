from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

# Найти поле ввода текста
input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
# Введите в поле текст 1000
input_field.send_keys("1000")

sleep(2)

# Очистите это поле (метод clear)
input_field.clear()

sleep(2)

# Введите в поле текст 999
input_field.send_keys("999")

driver.quit()
