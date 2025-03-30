import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Filtered_product_page(Base):
    """Класс страницы с отфильтрованным продуктом"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    drying_machine = "//div[@id='node-19065']"
    product_for_count = "[class*='node-product']"

    # Getters

    def get_drying_machine(self):
        """Ожидает появления и кликабельности отфильтрованного продукта"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.drying_machine)))

    # Actions
    def click_drying_machine(self):
        """Кликает по отфильтрованному продукту"""
        self.get_drying_machine().click()
        print("Click drying machine")

    # Methods
    def select_drying_machine(self):
        count_product = self.get_product_count(
            product_selector=self.product_for_count)  # Считаем количество продуктов после фильтрации
        if count_product == 1:
            self.click_drying_machine()  # Кликаем по отфильтрованному продукту
        else:
            print(f'Счетчик продуктов после фильтрации {count_product}, должен быть 1')
            pytest.fail()
