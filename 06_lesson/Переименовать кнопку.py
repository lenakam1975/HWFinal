from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/textinput")

# Укажите в поле ввода текст SkyPro.
element = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
element.send_keys("SkyPro")

# Нажмите на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Получите текст кнопки и выведите в консоль ("SkyPro")
txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()
