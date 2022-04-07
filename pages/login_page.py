from pages.base_page import BasePage

from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.url, "login is absent in current url"
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "Password form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISER_FORM_EMAIL), "Register email form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISER_FORM_PASSWORD), "Register Password form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISER_FORM_PASSWORD2), "Register2 Password form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISER_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISER_FORM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISER_FORM_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_REGISTER).click()