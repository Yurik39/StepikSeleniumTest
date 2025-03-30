from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from helpers import constants


class Cart_page(Base):
    """Класс страницы корзины"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    order_button_without_registration = "//input[@id='edit-shop-cart-actions-order-no-registration']"
    price_value = "//td[@class='col-price']"

    # Getters
    def get_order_button_without_registration(self):
        """Ожидает появления и кликабельности кнопки 'Оформить без регистрации'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.order_button_without_registration)))

    def get_price_value(self):
        """Ожидает появления цены товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_value)))

    # Actions
    def click_order_button_without_registration(self):
        """Кликает по кнопке 'Оформить без регистрации'"""
        self.get_order_button_without_registration().click()
        print("Click order button without registration")

    # Methods
    def select_order_button_without_registration(self):
        self.assert_word(self.get_price_value(), constants.price)  # Проверяем корректность цены товара
        self.click_order_button_without_registration()  # Кликаем по кнопке Оформить без регистрации
