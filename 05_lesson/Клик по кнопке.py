from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# 1. зайти на сайт

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликните на кнопку Add Element
for x in range(5):
    driver.find_element(
        By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()

    # Соберите со страницы список кнопок Delete
    button_delete = driver.find_elements(
        By.CSS_SELECTOR, 'button[class="added-manually"]')

    # Выведите на экран размер списка.
    print("Размер списка:", len(button_delete))

sleep(2)
