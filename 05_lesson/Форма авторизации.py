from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

# Найти поле ввода текста
input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
)

# В поле username введите значение tomsmith
input_field.send_keys("tomsmith")

# В поле password введите значение SuperSecretPassword!
input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
)

input_field.send_keys("SuperSecretPassword!")

# Нажмите кнопку Login
button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.radius'))
)

button.click()
