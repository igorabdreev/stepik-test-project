from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

class AddPageLocators():
    ADD_BOOK = (By.CSS_SELECTOR, "#add_to_basket_form")



