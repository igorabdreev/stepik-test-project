from selenium.webdriver.common.by import By
import pytest
from pages.base_page import BasePage
# py -m pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.basket_page import BasketPage

#def go_to_login_page(browser):
    #login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    #login_link.click()

 # путест вызывает только эту функцию, т.к. она она начинается на TEST...




#def test_guest_can_go_to_login_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.open()  # открываем страницу
    #page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
      #login_page = page.go_to_login_page() #Для первого метода
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()


#def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/"
    #page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    #page.open()  # открываем страницу
    #page.go_to_basket_page()
    #basket_page = BasketPage(browser, browser.current_url)  # Объект страницы корзины
    #basket_page.should_not_be_product_in_basket()  # Ожидаем, что в корзине нет товаров
    #basket_page.basket_is_empty()  # Ожидаем, что есть текст о том что корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasePage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)  # Объект страницы корзины
    basket_page.should_not_be_product_in_basket()  # Ожидаем, что в корзине нет товаров
    basket_page.basket_is_empty()  # Ожидаем, что есть текст о том что корзина пуста