import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Calculator_class import Calculator
from Shop_class import Authorization
from Shop_class import MainPage
from Shop_class import CartPage
from Shop_class import FormPage

@allure.epic("Калькулятор")
@allure.severity("blocker")
@allure.id("CALK-1")
@allure.title("работа основного функционала калькулятора")
@allure.story("работа функциональности калькулятора на сайте")
@allure.feature("Калькулятор")
@allure.description("работа функциональности калькулятора на сайте")
def test_calculator():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    calculator = Calculator(driver)
    calculator.set_delay(45)
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    result = WebDriverWait(driver, 45).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class='screen' and text()='15']")))
    assert result.text == "15", f"Ожидалось '15', получено '{result.text}'"
    print(result.text)

    driver.quit()


@allure.epic("Магазин")
@allure.severity("blocker")
@allure.id("SHOP-1")
@allure.title("Авторизация и оформление покупки в корзине магазина")
@allure.story("Работа функциональности интернет-магазина на сайте")
@allure.feature("Магазин")
@allure.description("Проверка основного функционала в интернет-магазине")
def test_shop():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    # Авторизация
    shop = Authorization(driver)
    shop.input_text("user-name", 'standard_user')
    shop.input_text("password", 'secret_sauce')
    shop.click_element('login-button')

    # Добавление товара в корзину
    shop = MainPage(driver)
    shop.add_to_cart('add-to-cart-sauce-labs-backpack')
    shop.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    shop.add_to_cart('add-to-cart-sauce-labs-onesie')
    shop.add_to_cart('shopping-cart-link')

    # Нажать кнопку Checkout
    shop = CartPage(driver)
    shop.checkout('checkout')

    # Заполнить поля
    shop = FormPage(driver)
    shop.input_field('first-name', "Elena")
    shop.input_field('last-name', "G")
    shop.input_field('postal-code', "123456")
    shop.click_button('continue')

    # Ожидаемый результат
    result = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, 'summary_total_label'))
    )
    print(result.text)
    assert result.text == "Total: $58.29", \
        f"Ожидаемая итоговая сумма: $58.29, полученная сумма: {result.text}"

    driver.quit()