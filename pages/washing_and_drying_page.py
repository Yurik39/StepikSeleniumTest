from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Washing_and_drying_page(Base):
    """Класс страницы 'Стирка и сушка'"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    drying = "//div[@id='taxonomy-term-384']"
    value_word = "//div[@id='block-features-page-title']"

    # Getters

    def get_value_word(self):
        """Ожидает появления тайтла Стирка и сушка"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.value_word)))

    def get_drying_category(self):
        """Ожидает появления и кликабельности баннера 'Сушильные машины'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.drying)))

    # Actions
    def click_drying_category(self):
        """Кликает по баннеру 'Сушильные машины'"""
        self.get_drying_category().click()
        print("Click drying category")

    # Methods
    def select_drying_category(self):
        self.assert_word(self.get_value_word(), "Стирка и сушка")  # Проверяем наличие тайтла Стирка и сушка
        self.click_drying_category()  # Переходим на страницу Сушильные машины
