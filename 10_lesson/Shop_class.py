import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Authorization:
    def __init__(self, driver):
        """ Конструктор выполняет следующие основные задачи:
            Присваивает драйвер текущему экземпляру класса.
            Устанавливает неявное ожидание.
            Переходит на стартовую страницу авторизации www.saucedemo.com.
            Максимизирует окно браузера.
        """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()

    @allure.step("Auth. Авторизация")
    def input_text(self, id_element: str, text: str) -> None:
        """ Метод находит элемент на странице
            по уникальному идентификатору элемента id_element.
            Отправляет текст в найденный элемент методом send_keys().
        """
        with allure.step("Auth. Найти элемент по ID для ввода данных"):
            input_field = self.driver.find_element(By.ID, id_element)
            input_field.clear()  # Очищаем поле перед вводом
        with allure.step(
                "Auth. Внести в найденный элемент "
                "данные пользователя - логин, пароль"):
            input_field.send_keys(text)

    @allure.step("Auth. Авторизация")
    def click_element(self, id_element: str) -> None:
        """ Метод имитирует клик по элементу
            с уникальным идентификатором id_element.
        """
        with allure.step("Auth. Кликнуть по элементу с уникальным ID"):
            button = self.driver.find_element(By.ID, id_element)
            button.click()


class MainPage:
    def __init__(self, driver):
        """ Конструктор выполняет следующие основные задачи:
            Присваивает драйвер текущему экземпляру
            класса (self.driver = driver).
            Устанавливает неявное ожидание в 20 секунд (implicitly_wait(20)).
            Переходит на страницу www.saucedemo.com/inventory.html.
            Максимизирует окно браузера.
        """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/inventory.html")
        self.driver.maximize_window()

    @allure.step("MainPage. Добавить товар в корзину")
    def add_to_cart(self, name: str) -> None:
        """ Метод служит для добавления товара в корзину на веб-сайте,
            выполняя клик по соответствующей кнопке.
            Товар определяется по имени, переданному в качестве аргумента name.
        """
        with allure.step(
                "MainPage. Найти на странице элемент "
                "по XPath выражению"):
            button = self.driver.find_element(
                By.XPATH, f"//*[@data-test='{name}']")
        with allure.step("MainPage. Кликнуть по кнопке найденного элемента"):
            button.click()


class CartPage:
    def __init__(self, driver):
        """ Конструктор выполняет следующие основные задачи:
            Присваивает драйвер текущему экземпляру
            класса (self.driver = driver).
            Устанавливает неявное ожидание в 20 секунд (implicitly_wait(20)).
            Переходит на страницу www.saucedemo.com/cart.html.
            Максимизирует окно браузера.
        """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/cart.html")
        self.driver.maximize_window()

    @allure.step("CartPage. Кликнуть по элементу с ID {button}")
    def checkout(self, button: str) -> None:
        """ Метод имитирует клик по элементу
            с уникальным идентификатором button.
        """
        with allure.step("CartPage. Найти элемент на странице по ID"):
            checkout = self.driver.find_element(By.ID, f"{button}")
        with allure.step("CartPage. Кликнуть по кнопке с ID button"):
            checkout.click()


class FormPage:
    def __init__(self, driver):
        """ Конструктор выполняет следующие основные задачи:
            Присваивает драйвер текущему экземпляру
            класса (self.driver = driver).
            Устанавливает неявное ожидание.
            Максимизирует окно браузера.
        """
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
        self.driver.maximize_window()

    @allure.step(
        "FormPage. Заполнить форму данными пользователя "
        "и проверить итоговую сумму")
    def input_field(self, id_element: str, text: str) -> None:
        """ Метод служит для заполнения формы данными
            (имя, фамилия, почтовый индекс)
            и проверки итоговой стоимости.
            Результат печатается в консоль.
        """
        with allure.step("FormPage. Найти элемент по ID для ввода данных"):
            wait = WebDriverWait(self.driver, 10)
            input_field = wait.until(EC.visibility_of_element_located((By.ID, id_element)))
        with allure.step(
                "FormPage. Внести в найденный элемент данными пользователя: "
                "имя, фамилия, почтовый индекс"):
            input_field.send_keys(text)

    @allure.step("FormPage. Кликнуть по элементу с ID {id_element}")
    def click_button(self, id_element: str) -> None:
        """ Метод имитирует клик по элементу
            с уникальным идентификатором id_element.
        """
        with allure.step("FormPage. Найти элемент по ID"):
            click_button = self.driver.find_element(By.ID, f"{id_element}")
        with allure.step("FormPage. Кликнуть по найденному элементу"):
            click_button.click()
