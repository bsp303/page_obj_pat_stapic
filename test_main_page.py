import time
# испортируем класс LoginPage из файла login_page.py
import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/" # Задаем основную ссылку (ссылка откроется после запуска браузера)
        page = LoginPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()    # Открываем страницу
        page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_url()

class TestToEmptyBasket():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.check_basket()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.check_basket()