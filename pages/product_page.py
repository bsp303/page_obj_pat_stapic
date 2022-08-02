import time
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    # метод добавления в корзину
    def add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART_3), "кнопка Добавить в корзину не найдена"
        ADD_CART = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART_3)
        ADD_CART.click()
        print("Нажата кнопка добавления в корзину")
        self.solve_quiz_and_get_code()
        print("Введен код подтверждения")

    # метод проверки названия книги с тем что добавлено в корзину
    def check_to_title(self):
        # Берем текст книги с страницы
        TITLE_BOOK = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_MARKET)
        # Берем текст книги с алерта добавления
        ALLERT_BOOK = self.browser.find_element(*ProductPageLocators.TITLE_BOOK_ALLERT)
        assert TITLE_BOOK.text == ALLERT_BOOK.text, "увы но не совпал текст книги тем что в аллерте"
        print("в корзину добавлен товар с названием:", TITLE_BOOK.text)

    # метод проверки стоимости книги и стоимостью корзины
    def check_to_price(self):
        # Берем основную цену книги
        MAIN_PRICE_BOOK = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_MARKET)
        # Берем цену сформированной корзины
        CART_PRICE_BOOK = self.browser.find_element(*ProductPageLocators.PRICE_BOOK_CART)
        assert MAIN_PRICE_BOOK.text == CART_PRICE_BOOK.text, "увы но не совпал стоимость книги с стоимостью корзины"
        print("Стоимость корзины =", CART_PRICE_BOOK.text)
        time.sleep(0)

    # метод проверки отсутсвия блока об успешном добавлении
    def should_not_be_success_massage(self):
        assert self.is_not_element_present(*ProductPageLocators.TITLE_BOOK_ALLERT), "присутствует блок об успешном добавлении"

    # метод проверки отображения блока об успешном добавлении
    def should_be_success_massage(self):
        assert self.is_element_present(*ProductPageLocators.TITLE_BOOK_ALLERT)

    # метод исчезновения сообщения с названием книги
    def should_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.TITLE_BOOK_ALLERT)