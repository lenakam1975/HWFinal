from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.implicitly_wait(15)
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

elements = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Done"))

image = WebDriverWait(driver, 20).until(
    EC.visibility_of_all_elements_located((By.TAG_NAME, 'img'))
)

src = image[3].get_attribute("src")

print(src)

driver.quit()
