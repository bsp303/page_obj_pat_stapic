from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def check_basket(self):
        self.check_open_basket_page()
        self.check_the_absent_of_block_with_products()
        self.check_the_basket_is_empty()

    def check_open_basket_page(self):
        assert self.is_element_present(*BasePageLocators.TITLE_BASKET_PAGE)
        print("Открыта страница корзины")

    def check_the_absent_of_block_with_products(self):
        assert self.is_not_element_present(*BasePageLocators.BLOCK_THE_PRODUCTS)
        print("Блок с товарами отсутствует в корзине")

    def check_the_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.MASSAGE_EMPTY_BASKET)
        print("Отображен текст о том что корзина пуска")