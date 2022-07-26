import time

from pages.locators import BasePageLocators
from .pages.product_page import ProductPage
def test_guest_should_see_login_link_on_product_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" # Задаем основную ссылку (ссылка откроется после запуска браузера)
    page = ProductPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # Открываем страницу
    page.go_to_basket_page()
    assert page.is_not_element_present(*BasePageLocators.BLOCK_THE_PRODUCTS)
    assert page.is_element_present(*BasePageLocators.MASSAGE_EMPTY_BASKET)
    print("Отображен текст о том что корзина пуска")
    time.sleep(10)