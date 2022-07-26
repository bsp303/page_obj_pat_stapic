from pages.locators import ProductPageLocators
from pages.base_page import BasePage
import time
from .pages.product_page import ProductPage
import pytest
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.TITLE_BOOK_ALLERT)
    print("Первый кейс")

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.TITLE_BOOK_ALLERT)
    print("Второй кейс")

def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    assert page.is_disappeared(*ProductPageLocators.TITLE_BOOK_ALLERT)
    print("Третий кейс")
