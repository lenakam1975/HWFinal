from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.implicitly_wait(20)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    # В поле ввода по локатору #delay введите значение 45.
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажмите на кнопки: 7 + 8 =
    seven_button = driver.find_element(
        By.XPATH, "//div[@class='keys']/span[1]")
    seven_button.click()

    plus_button = driver.find_element(By.XPATH, "//div[@class='keys']/span[4]")
    plus_button.click()

    eight_button = driver.find_element(
        By.XPATH, "//div[@class='keys']/span[2]")
    eight_button.click()

    equals_button = driver.find_element(
        By.XPATH, "//div[@class='keys']/span[15]")
    equals_button.click()

    # Проскролить вверх
    driver.execute_script("window.scrollBy(0, 800)")

    # Ожидание результата
    locator = (By.XPATH, "//div[@class='screen' and text()='15']")
    WebDriverWait(driver, 45).until(EC.presence_of_element_located(locator))

    # Проверка результата
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15", f"Ожидалось '15', получено '{result}'"

    # Закрываем браузер после завершения теста
    driver.quit()
