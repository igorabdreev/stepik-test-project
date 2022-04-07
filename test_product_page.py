from selenium.webdriver.common.by import By
# py -m pytest -v --tb=line --language=en test_main_page.py
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from pages.login_page import LoginPage

from pages.product_page import ProductPage
import pytest
import time
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = "tester123456789"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):  # добавил линк Link
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # page.get(link)
        page.open()  # открываем страницу
        page.add_to_cart()
        #page.solve_quiz_and_get_code()
        page.should_be_message_about_adding()
        page.should_be_message_about_same_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        page = ProductPage(self.browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        # page.get(link)
        page.open()  # открываем страницу
        page.should_not_be_success_message()
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):  # добавил линк Link
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
            # page.get(link)
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
            # time.sleep(11000)
            # py -m pytest -s test_product_page.py

@pytest.mark.xfail  # Помечаем тест как нормально падающий
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
            # Открываем страницу товара
            # Добавляем товар в корзину
            # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
            # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
            # page.get(link)
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
@pytest.mark.need_review
def test_guest_cant_see_success_message(browser):
            # Открываем страницу товара
            # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page = ProductPage(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
            # page.get(link)
    page.open()  # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
            # Открываем страницу товара
            # Добавляем товар в корзину
            # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page = ProductPage(browser,
                               link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
            # page.get(link)
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()

@pytest.mark.need_review
def test_guest_should_see_login_link_on_product_page(browser):
            # Убеждаемся что ссылка на страницу логина есть
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
            # Переходим на страницу логина
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser,
                            link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)  # Объект страницы корзины
    basket_page.should_not_be_product_in_basket()  # Ожидаем, что в корзине нет товаров
    basket_page.basket_is_empty()  # Ожидаем, что есть текст о том что корзина пуста

        #py -m pytest -s test_product_page.py
        #py -m pytest -v --tb=line --language=en -m need_review