from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from conftest import set_up
from pages.cart_page import Cart_page
from pages.filtered_product_page import Filtered_product_page
from pages.filters_page import Filters_page
from pages.main_page import Main_page
from pages.order_page import Order_page
from pages.product_page import Product_page
from pages.washing_and_drying_page import Washing_and_drying_page


def test_making_a_purchase(set_up):
    # Настройки вебдрайвера
    options = webdriver.ChromeOptions()  # Возможность добавлять дополнтельные настройки для браузера
    options.add_experimental_option('detach', False)  # Опция которая не позволит браузеру закрыться
    options.page_load_strategy = "eager"
    service = ChromeService(executable_path="C:\\Users\\Home\\PycharmProjects\\resource\\yandexdriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    base_url = 'https://greenwest39.ru/'
    driver.get(base_url)

    # Открываем главную страницу и выбираем категорию Стирка и сушка
    mp = Main_page(driver)
    mp.select_washing_and_drying_category()

    # Выбираем категорию Сушильные машины
    wadp = Washing_and_drying_page(driver)
    wadp.select_drying_category()

    # Отфильтровываем конкретный продукт
    fp = Filters_page(driver)
    fp.select_filters_for_drying_machine_gorenje()

    # Кликаем по продукту
    fpp = Filtered_product_page(driver)
    fpp.select_drying_machine()

    # Добавляем продукт в корзину
    pp = Product_page(driver)
    pp.select_submit_button()

    # Кликаем по кнопке Оформление без регистрации
    cp = Cart_page(driver)
    cp.select_order_button_without_registration()

    # Вводим данные и подтверждаем заказ
    op = Order_page(driver)
    op.select_confirm_order()
