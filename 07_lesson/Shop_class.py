from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Authorization:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    def set_delay(self, id, text):
        delay_input = self.driver.find_element(By.ID, f"{id}")
        delay_input.send_keys(f"{text}")
        button = self.driver.find_element(By.ID, f"{id}")
        button.click()


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.maximize_window()

    def add_to_cart(self, name):
        button = self.driver.find_element(
            By.XPATH, f"//*[@data-test='{name}']")
        button.click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.maximize_window()

    def checkout(self, button):
        checkout = self.driver.find_element(By.ID, f"{button}")
        checkout.click()


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.maximize_window()

    def input_field(self, id, text):
        input_field = self.driver.find_element(By.ID, f"{id}")
        input_field.send_keys(f'{text}')
        button_continue = self.driver.find_element(By.ID, f"{id}")
        button_continue.click()

    def result(self):
        results = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, 'summary_total_label')))
        print(results.text)
        assert results.text == "Total: $58.29", \
            f"Ожидаемая итоговая сумма: $58.29, полученная сумма: {results}"
