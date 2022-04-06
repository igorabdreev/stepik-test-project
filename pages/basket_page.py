from pages.base_page import BasePage
from pages.locators import BasketIsEmpty
from pages.locators import BasePageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        #assert self.is_element_present(*BasePageLocators.BASKET_BUTTON), (
            #"basket button is not presented")
        # Проверяем что кнопка есть
        def should_be_message_about_empty_basket(self):
            """Ожидаем, что есть текст о том что корзина пуста
            """
            text_about_empty_basket = self.browser.find_element(
                *BasketIsEmpty.BASKET_EMPTY_TEXT).text
            assert text_about_empty_basket == "Your basket is empty. Continue shopping", (
                "Text about empty basket is not present")

    def should_not_be_product_in_basket(self):
        #Ожидаем, что в корзине нет товаров

        assert self.is_not_element_present(*BasketIsEmpty.BASKET_PRODUCT_NAME), (
            "Name of product is presented, but should not be")