from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):
    "Класс главной страницы"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    washing_and_drying = "//div[@id='taxonomy-term-377']"
    value_url = "https://greenwest39.ru/"
    cookie_button = "//a[@class='personal-data-agreement-cookie-ok form-submit']"

    # Getters

    def get_washing_and_drying_category(self):
        """Ожидает появления и кликабельности баннера 'Стирка и сушка'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.washing_and_drying)))

    def get_cookie_button(self):
        """Ожидает появления и кликабельности кнопки 'ОК'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cookie_button)))

    # Actions
    def click_washing_and_drying_category(self):
        """Кликает по баннеру 'Стирка и сушка'"""
        self.get_washing_and_drying_category().click()
        print("Click washing and drying category")

    def click_cookie_button(self):
        """Кликает по кнопке 'ОК' на всплывабщей панели о куках"""
        self.get_cookie_button().click()
        print("Click cookie button")

    # Methods
    def select_washing_and_drying_category(self):
        self.click_cookie_button()  # Принимаем уведомление о куках
        self.assert_url(self.value_url, self.get_current_url())  # Проверяем URL главной страницы
        self.click_washing_and_drying_category()  # Переходим на страницу Стиральные и сушильные машины
