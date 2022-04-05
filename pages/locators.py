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
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1") # название книги
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong") # название книги которое было добавлено
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

#class ProductPageLocators():
    #SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#add_to_basket_form")