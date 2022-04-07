from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISER_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name=registration_submit]")

class AddPageLocators():
    ADD_BOOK = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1") # название книги
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alertinner strong") # название книги которое было добавлено
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main p")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    BASKET_BUTTON_INVALID = (By.CSS_SELECTOR, ".basket-mini_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketIsEmpty():
    BasketIsEmptyText = (By.CSS_SELECTOR, "#content_inner p")

    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items h3")