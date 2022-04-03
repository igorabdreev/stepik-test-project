from selenium.webdriver.common.by import By
# py -m pytest -v --tb=line --language=en test_main_page.py
from pages.main_page import MainPage
from pages.login_page import LoginPage


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

 # путест вызывает только эту функцию, т.к. она она начинается на TEST...




def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    #login_page = page.go_to_login_page() #Для первого метода
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
