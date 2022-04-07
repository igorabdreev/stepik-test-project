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
