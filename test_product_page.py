from selenium.webdriver.common.by import By
# py -m pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.product_page import ProductPage
import pytest
import time
link= "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser): #добавил линк Link
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.get(link)
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    #time.sleep(11000)
    #py -m pytest -s test_product_page.py
@pytest.mark.xfail            # Помечаем тест как нормально падающий
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.get(link)
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
# Открываем страницу товара
# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.get(link)
    page.open()  # открываем страницу
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
#Открываем страницу товара
#Добавляем товар в корзину
#Проверяем, что нет сообщения об успехе с помощью is_disappeared
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.get(link)
    page.open()  # открываем страницу
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()