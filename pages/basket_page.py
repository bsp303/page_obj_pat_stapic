from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    # метод запускающий все проверки последовательно
    def check_basket(self):
        self.check_open_basket_page()
        self.check_the_absent_of_block_with_products()
        self.check_text_basket_is_empty()

    # проверка нахождения на сранице корзина
    def check_open_basket_page(self):
        assert self.is_element_present(*BasePageLocators.TITLE_BASKET_PAGE)
        print("Открыта страница корзины")

    # проверка отсутствия в корзине товаров
    def check_the_absent_of_block_with_products(self):
        assert self.is_not_element_present(*BasePageLocators.BLOCK_THE_PRODUCTS)
        print("Блок с товарами отсутствует в корзине")

    # проверка наличия текста о пустой корзине
    def check_text_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.MASSAGE_EMPTY_BASKET)
        print("Отображен текст о том что корзина пуска")