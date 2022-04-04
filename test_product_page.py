from selenium.webdriver.common.by import By
# py -m pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.product_page import ProductPage
import time
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    #time.sleep(11000)
    #py -m pytest -s test_product_page.py