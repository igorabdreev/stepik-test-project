from .base_page import BasePage
from pages.locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url(), "login is absent in current url"
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM_EMAIL), "Login form is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM_PASSWORD), "Password form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISER_FORM_EMAIL), "Register email form is not presented"
        assert self.is_element_present(*MainPageLocators.REGISER_FORM_PASSWORD), "Register Password form is not presented"
        assert self.is_element_present(*MainPageLocators.REGISER_FORM_PASSWORD2), "Register2 Password form is not presented"
