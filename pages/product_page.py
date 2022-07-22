import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
            assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART_3), "кнопка Добавить в корзину не найдена"
            ADD_CART = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART_3)
            ADD_CART.click()
            print("Нажата кнопка добавления в корзину")
            self.solve_quiz_and_get_code()
            print("Введен код подтверждения")
    def check_to_title(self):
            # Берем текст книги с страницы
            TITLE_BOOK = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_MARKET)
            # Берем текст книги с алерта добавления
            ALLERT_BOOK = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_ALLERT)
            assert TITLE_BOOK.text == ALLERT_BOOK.text, "увы но не совпал текст книги тем что в аллерте"
            print("в корзину добавлен товар с названием:", TITLE_BOOK.text)
    def check_to_price(self):
            # Берем основную цену книги
            MAIN_PRICE_BOOK = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_MARKET)
            # Берем цену сформированной корзины
            CART_PRICE_BOOK = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_CART)
            assert MAIN_PRICE_BOOK.text == CART_PRICE_BOOK.text, "увы но не совпал стоимость книги с стоимостью корзины"
            print("Стоимость корзины =", CART_PRICE_BOOK.text)
            time.sleep(0)
