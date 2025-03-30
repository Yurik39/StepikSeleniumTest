from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from helpers import constants


class Product_page(Base):
    """Класс страницы с продуктом"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    submit_button = "//input[@id='edit-submit']"
    manufacturer_value_text = f'//div[contains(text(), "{constants.manufacturer}")]'
    deep_value_text = f'//div[contains(text(), "{constants.min_deep}")]'
    brand_value_text = "//h1[@class='node-title']"

    # Getters

    def get_submit_button(self):
        """Ожидает появления и кликабельности кнопки 'В корзину'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_manufacturer_value_text(self):
        """Ожидает появления текста производителя"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.manufacturer_value_text)))

    def get_deep_value_text(self):
        """Ожидает появления текста глубины"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.deep_value_text)))

    def get_brand_value_text(self):
        """Ожидает появления текста бренда"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.brand_value_text)))

    # Actions
    def click_submit_button(self):
        """Кликает по кнопке 'В корзину'"""
        self.get_submit_button().click()
        print("Click submit button")

    # Methods
    def select_submit_button(self):
        self.assert_word(self.get_manufacturer_value_text(),
                         constants.manufacturer)  # Проверяем наличие отфильтрованнного текста производителя
        self.assert_in_word(self.get_deep_value_text(),
                            constants.min_deep)  # Проверяем наличие отфильтрованнного текста глубины
        self.assert_in_word(self.get_brand_value_text(),
                            constants.brand)  # Проверяем наличие отфильтрованнного текста бренда
        self.click_submit_button()  # Кликаем по кнопке В Корзину
