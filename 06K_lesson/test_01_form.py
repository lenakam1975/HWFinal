from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    # Открыть страницу в браузере.
    driver.implicitly_wait(15)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()

    # Заполните форму значениям.
    first_name_field = driver.find_element(By.NAME, "first-name")
    first_name_field.send_keys("Иван")
    last_name_field = driver.find_element(By.NAME, "last-name")
    last_name_field.send_keys("Петров")
    address_field = driver.find_element(By.NAME, "address")
    address_field.send_keys("Ленина, 55-3")
    email_field = driver.find_element(By.NAME, "e-mail")
    email_field.send_keys("test@skypro.com")
    phone_number_field = driver.find_element(By.NAME, "phone")
    phone_number_field.send_keys("+7985899998787")
    city_field = driver.find_element(By.NAME, "city")
    city_field.send_keys("Москва")
    country_field = driver.find_element(By.NAME, "country")
    country_field.send_keys("Россия")
    job_position_field = driver.find_element(By.NAME, "job-position")
    job_position_field.send_keys("QA")
    company_field = driver.find_element(By.NAME, "company")
    company_field.send_keys("SkyPro")

    # Оставляем поле Zip Code пустым
    zip_code_field = driver.find_element(By.NAME, "zip-code")
    zip_code_field.clear()

    # Проскролить вверх
    driver.execute_script("window.scrollBy(0, 1000)")

    # Ожидание кнопки
    locator = (By.CSS_SELECTOR, 'button[type="submit"]')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))

    # Нажмите кнопку Submit.
    submit_button = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    # Проскролить вверх
    driver.execute_script("window.scrollBy(0, 1000)")

    sleep(10)

    # Проверьте (assert), что поле Zip code подсвечено красным.

    zip_code_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'zip-code'))
    )
    zip_code_red = zip_code_field.value_of_css_property('border-color')
    assert zip_code_red == "rgb(245, 194, 199)", \
        (f'Поле Zip code подсвечено красным: {zip_code_red}, '
         f'ожидалось: rgb(245, 194, 199)')

    # Проверка подсветки остальных полей
    green_poles = [
        "#first_name_field",
        "#last_name_field",
        "#address_field",
        "#email_field",
        "#phone_number_field",
        "#city_field",
        "#country_field",
        "#job_position_field",
        "#company_field"]
    for pole in green_poles:
        element = driver.find_element(
            By.CSS_SELECTOR, 'div[class="alert py-2 alert-success"]')
        assert "rgb(186, 219, 204)" == element.value_of_css_property(
            'border-color'), f"Поле {pole} не подсвечено зеленым"

    # Закрываем браузер после завершения теста
    driver.quit()
