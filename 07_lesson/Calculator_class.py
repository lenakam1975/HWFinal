from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.maximize_window()

    def set_delay(self, delay):
        set_delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        set_delay.clear()
        set_delay.send_keys(delay)

    def click_button(self, button):
        click_button = self.driver.find_element(
            By.XPATH, f"//div[@class='keys']/span[text()='{button}']")
        click_button.click()

    def set_result(self, driver):
        locator = (By.XPATH, "//div[@class='screen' and text()='15']")
        WebDriverWait(driver, 45).until(
            EC.presence_of_element_located(locator))
        result = driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert result == "15", f"Ожидалось '15', получено '{result}'"

        driver.quit()
