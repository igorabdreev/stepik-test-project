from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from pages.login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        pass
        #def __init__(self, *args, **kwargs):
            #super(MainPage, self).__init__(*args, **kwargs)
        #link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        #link.click()
        #Так как внесли этот метод в base_page то тут он не нужен, ставим заглушку...

        #return LoginPage(browser=self.browser, url=self.browser.current_url)
        # Возвращаем LoginPage

        # from pages.base_page import BasePage Указал путь вместе с папкой при импорте класса в файле main_page.py.

    #def should_be_login_link(self):
        #assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"