from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    # Откройте сайт магазина: https://www.saucedemo.com/.
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.implicitly_wait(20)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Авторизуйтесь как пользователь standard_user.
    delay_input = driver.find_element(By.ID, "user-name")
    delay_input.send_keys("standard_user")

    delay_input = driver.find_element(By.ID, "password")
    delay_input.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    sleep(2)

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.
    # Sauce Labs Bolt T-Shirt.
    # Sauce Labs Onesie.

    backpack_button = driver.find_element(
        By.NAME, "add-to-cart-sauce-labs-backpack")
    backpack_button.click()

    t_shirt_button = driver.find_element(
        By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    t_shirt_button.click()

    onesie_button = driver.find_element(
        By.NAME, "add-to-cart-sauce-labs-onesie")
    onesie_button.click()

    # Перейдите в корзину.
    cart_container = driver.find_element(By.ID, "shopping_cart_container")
    cart_container.click()

    # Нажмите Checkout.
    checkout = driver.find_element(By.ID, "checkout")
    checkout.click()

    # Заполните форму своими данными: имя, фамилия, почтовый индекс.
    input_field = driver.find_element(By.NAME, 'firstName')
    input_field.send_keys('Elena')

    input_field = driver.find_element(By.NAME, 'lastName')
    input_field.send_keys('G')

    input_field = driver.find_element(By.NAME, 'postalCode')
    input_field.send_keys('123456')

    # Нажмите кнопку Continue.
    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    # Проскролить вверх
    driver.execute_script("window.scrollBy(0, 200)")
    sleep(2)

    # Прочитайте со страницы итоговую стоимость (Total).
    results = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, 'summary_total_label')))
    print(results.text)

    # Проверьте, что итоговая сумма равна $58.29.
    assert results.text == "Total: $58.29", \
        f"Ожидаемая итоговая сумма: $58.29, полученная сумма: {results}"

    # Закройте браузер.
    driver.quit()
