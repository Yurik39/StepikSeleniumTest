from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from helpers import constants


class Filters_page(Base):
    """Класс с фильтрами"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filter_manufacturer = "//fieldset[@id='edit-filters-f-1-4']"
    filter_manufacturer_slovenia = "//label[@for='edit-filters-f-1-4-vars-6']"
    filter_depth = "//*[@id='edit-filters-f-1-9']/legend/span/a"
    filter_depth_data_min = "//input[@id='edit-filters-f-1-9-slider-left']"
    filter_depth_data_max = "//input[@id='edit-filters-f-1-9-slider-right']"
    filter_brand = "//*[@id='edit-filters-t-2']/legend/span/a"
    filter_brand_gorenje = "//label[@for='edit-filters-t-2-tid-110']"
    filter_accept_button = "//input[@id='edit-submit--28']"
    filter_block = "#block-node-specifications-node-filters .content"

    # Getters

    def get_filter_manufacturer(self):
        """Ожидает появления и кликабельности фильтра 'Производитель'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer)))

    def get_filter_manufacturer_slovenia(self):
        """Ожидает появления и кликабельности фильтра 'Словения'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_manufacturer_slovenia)))

    def get_filter_depth(self):
        """Ожидает появления и кликабельности фильтра 'Глубина'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_depth)))

    def get_filter_depth_data_min(self):
        """Ожидает появления и кликабельности фильтра 'Глубина ОТ:'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_depth_data_min)))

    def get_filter_depth_data_max(self):
        """Ожидает появления и кликабельности фильтра 'Глубина ДО:'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_depth_data_max)))

    def get_filter_brand(self):
        """Ожидает появления и кликабельности фильтра 'Бренд'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand)))

    def get_filter_brand_gorenje(self):
        """Ожидает появления и кликабельности фильтра 'Горенье'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_brand_gorenje)))

    def get_filter_accept_button(self):
        """Ожидает появления и кликабельности кнопки 'Показать'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_accept_button)))

    def get_scroll_filter_block(self):
        """Ожидает появления и скролла в блоке с фильтрами"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_block)))

    # Actions

    def click_filter_manufacturer(self):
        """Кликает по фильтру 'Производитель'"""
        self.get_filter_manufacturer().click()
        print("Click filter manufacturer")

    def click_filter_manufacturer_slovenia(self):
        """Кликает по фильтру 'Словения'"""
        self.get_filter_manufacturer_slovenia().click()
        print("Click filter manufacturer slovenia")

    def click_filter_depth(self):
        """Кликает по фильтру 'Глубина'"""
        self.get_filter_depth().click()
        print("Click filter depth")

    def input_filter_depth_data_min(self):
        """Вводит значение в фильтр 'Глубина ОТ:'"""
        self.get_filter_depth_data_min().clear()
        self.get_filter_depth_data_min().send_keys(constants.min_deep)
        print("Input filter depth data min")

    def input_filter_depth_data_max(self):
        """Вводит значение в фильтр 'Глубина ДО:'"""
        self.get_filter_depth_data_max().clear()
        self.get_filter_depth_data_max().send_keys(constants.max_deep)
        print("Input filter depth data max")

    def click_filter_brand(self):
        """Кликает по фильтру 'Бренд'"""
        self.get_filter_brand().click()
        print("Click filter brand")

    def click_filter_brand_gorenje(self):
        """Кликает по фильтру 'Горенье'"""
        self.get_filter_brand_gorenje().click()
        print("Click filter brand gorenje")

    def click_filter_accept_button(self):
        """Кликает по кнопке 'Показать'"""
        self.get_filter_accept_button().click()
        print("Click filter accept button")

    def scroll_to_end_filter_block(self):
        """Прокручивает до конца скролл в блоке фильтров"""
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.filter_block)
        print("Click filter accept button")

    # Methods
    def select_filters_for_drying_machine_gorenje(self):
        self.click_filter_manufacturer()  # Раскрываем фильтр Производитель
        self.click_filter_manufacturer_slovenia()  # Кликаем по фильтру Словения
        self.click_filter_depth()  # Раскрываем фильтр Глубина
        self.input_filter_depth_data_min()  # Вводим значение глубины min
        self.input_filter_depth_data_max()  # Вводим значение глубины max
        self.scroll_to_end_filter_block()  # Прокручиваем скролл фильтра до конца
        self.click_filter_brand()  # Раскрываем фильтр Бренд
        self.click_filter_brand_gorenje()  # Кликаем по фильтру Gorenje
        self.click_filter_accept_button()  # Кликаем по кнопке Показать
