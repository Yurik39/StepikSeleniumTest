from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from helpers import constants


class Order_page(Base):
    """Класс страницы с заказом"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    pickup_button = "//div[@id='edit-shop-cart-delivery-method']/div[2]"
    recipient_input = "//input[@id='edit-recipient-fields-lfm']"
    email_input = "//input[@id='edit-recipient-fields-mail']"
    phone_input = "//input[@id='edit-recipient-fields-phone']"
    discount_cart_input = "//input[@id='edit-field-nomer-karty-skidok-und-0-value']"
    promo_code_input = "//input[@id='edit-field-promo-kod-und-0-value']"
    price_value = "//td[@class='col-price']"
    personal_data_checkbox = "//input[@id='edit-personal-data-agreement']"

    # Getters

    def get_pickup_button(self):
        """Ожидает появления и кликабельности кнопки 'Самовывоз'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.pickup_button)))

    def get_recipient_input(self):
        """Ожидает появления и кликабельности поля ввода 'Получатель'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.recipient_input)))

    def get_email_input(self):
        """Ожидает появления и кликабельности поля ввода 'Email'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email_input)))

    def get_phone_input(self):
        """Ожидает появления и кликабельности поля ввода 'Номер телефона'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_input)))

    def get_discount_cart_input(self):
        """Ожидает появления и кликабельности поля ввода 'Номер карты скидок'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.discount_cart_input)))

    def get_promo_code_input(self):
        """Ожидает появления и кликабельности поля ввода 'Промокод'"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.promo_code_input)))

    def get_personal_data_checkbox(self):
        """Ожидает появления и кликабельности чекбокса о персональных данных"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.personal_data_checkbox)))

    def get_price_value(self):
        """Ожидает появления цены товара"""
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_value)))

    # Actions
    def click_pickup_button(self):
        """Кликает по кнопке 'Самовывоз'"""
        self.get_pickup_button().click()
        print("Click pickup button")

    def input_recipient_input(self):
        """Вводит информацию в поле ввода 'Получатель'"""
        self.get_recipient_input().send_keys('Ярослав')
        print("Recipient input")

    def input_email_input(self):
        """Вводит информацию в поле ввода 'Email'"""
        self.get_email_input().send_keys('Yar@ya.ru')
        print("Email input")

    def input_phone_input(self):
        """Вводит информацию в поле ввода 'Номер телефона'"""
        self.get_phone_input().send_keys('89224788522')
        print("Phone input")

    def input_discount_cart_input(self):
        """Вводит информацию в поле ввода 'Номер карты скидок'"""
        self.get_discount_cart_input().send_keys('777')
        print("Discount cart input")

    def input_promo_code_input(self):
        """Вводит информацию в поле ввода 'Промокод'"""
        self.get_promo_code_input().send_keys('SALE25')
        print("Promo code input")

    def click_personal_data_checkbox(self):
        """Кликает по чекбоксу согласия обработки персональных данных"""
        self.get_personal_data_checkbox().click()
        print("Click personal data checkbox")

    # Methods
    def select_confirm_order(self):
        self.assert_word(self.get_price_value(), constants.price)  # Проверяем корректность цены товара
        self.click_pickup_button()  # Кликаем по кнопке Самовывоз
        self.input_recipient_input()  # Вводим данные Получателя
        self.input_email_input()  # Вводим Емеил
        self.input_phone_input()  # Вводим номер телефона
        self.input_discount_cart_input()  # Вводим карту скидок
        self.input_promo_code_input()  # Вводим промокод
        data_agreement = self.get_checkbox_attribute_checked(self.personal_data_checkbox)
        if data_agreement == False:  # Если чекбокс не активен, кликаем по нему
            self.click_personal_data_checkbox()
            print("Подтвердить заказ")  # Имитируем подтверждение заказа
        else:
            print("Подтвердить заказ")  # Имитируем подтверждение заказа
