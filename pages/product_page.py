from pages.base_page import BasePage
from pages.locators import AddPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*AddPageLocators.ADD_BOOK)
        link.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*AddPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*AddPageLocators.PRODUCT_NAME_IN_MESSAGE), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*AddPageLocators.PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*AddPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        # Проверяем, что название товара в сообщении == названию товара на странице
        assert product_name == product_name_in_message, (
            "Product name does not match the message")

    def should_be_message_about_same_price(self):
        assert self.is_element_present(*AddPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        assert self.is_element_present(*AddPageLocators.PRODUCT_PRICE_BASKET), (
            "Product price in basket is not presented")
        # Затем получаем текст цены
        product_price = self.browser.find_element(*AddPageLocators.PRODUCT_PRICE).text
        product_price_in_basket = self.browser.find_element(*AddPageLocators.PRODUCT_PRICE_BASKET).text
        # Проверяем, что цена товара == цене товара в корзине
        assert product_price == product_price_in_basket, (
            "Price of the product does not match the price in the cart")
