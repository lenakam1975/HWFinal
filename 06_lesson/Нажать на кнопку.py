from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax")


# Нажмите на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получите текст из зеленой плашки.
# Выведите его в консоль ("Data loaded with AJAX get request.")
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()
