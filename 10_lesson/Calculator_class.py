import allure
from selenium.webdriver.common.by import By


class Calculator:
    """
        Конструктор выполняет следующие основные задачи:
        Сохраняет драйвер в поле класса.
        Устанавливает неявное ожидание.
        Переходит на нужную страницу с примером калькулятора.
        Максимизирует окно браузера.
    """
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self.driver.maximize_window()

    @allure.step("Calc. Ввести значение в поле задержки")
    def set_delay(self, delay: int) -> None:
        """ Метод находит элемент с ID "delay".
            Устанавливает задержку в секундах в форме на сайте.
            Целое число, представляющее количество секунд задержки.
            Очищает поле. Вводит новое значение, указанное в аргументе delay.
            Результат печатается в консоль.
        """
        with allure.step(
                "Calc. Найти элемент "
                "и установить задержку в поле ввода "
                "конкретного временного значения"):
            set_delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
            set_delay.clear()
        with allure.step("Calc. Ввести текст в поле"):
            set_delay.send_keys(delay)

    @allure.step("Calc. Нажать на кнопки калькулятора")
    def click_button(self, button: str) -> None:
        """ Метод предназначен для нажатия определенной кнопки на веб-странице
            по XPath выражению, фильтруя элементы по содержимому текста.
            Выполняем клик по найденной кнопке.
        """
        with allure.step(
                "Calc. Кликнуть по конкретной найденной "
                "кнопке по XPath выражению"):
            click_button = self.driver.find_element(
                By.XPATH, f"//div[@class='keys']/span[text()='{button}']")
            click_button.click()

