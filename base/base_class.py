from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Возвращает текущий URL"""
        get_url = self.driver.current_url
        return get_url

    def assert_word(self, word, result):
        """Проверяет корректность значения текста"""
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def assert_in_word(self, full_word, word_in):
        """Проверяет вхождение части текста"""
        value_word = full_word.text
        assert word_in in value_word
        print("Good value in word")

    def assert_url(self, url, result):
        """Проверяет корректность URL"""
        value_url = url
        assert value_url == result
        print("Good value url")

    def get_product_count(self, product_selector):
        """Возвращает количесвто видимых продуктов на странице"""
        visible_elements = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, product_selector)))
        return len(visible_elements)

    def get_checkbox_attribute_checked(self, checkbox_locator):
        """Возвращает булевое состояние чекбокса"""
        checkbox = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, checkbox_locator)))
        return checkbox.is_selected()
