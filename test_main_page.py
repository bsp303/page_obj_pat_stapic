import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/" # Задаем основную ссылку (ссылка откроется после запуска браузера)
        page = LoginPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # Открываем страницу
        page.go_to_login_page() # выполняем метод - переходим на страницу логина

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"  # Задаем основную ссылку (ссылка откроется после запуска браузера)
        page = LoginPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # Открываем страницу
        page.go_to_login_page() # выполняем метод - переходим на страницу логина

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"  # Задаем основную ссылку (ссылка откроется после запуска браузера)
        page = LoginPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # Открываем страницу
        page.should_be_login_url() # выполняем метод - проверки наличия ссылки на авторизацию/регистрацию

class TestToEmptyBasket():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"  # Задаем основную ссылку (ссылка откроется после запуска браузера)
        page = BasketPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # Открываем страницу
        page.go_to_basket_page() # выполняем метод - переход в корзину заказов
        page.check_basket() # выполняем список метод - проверка открытия станицы корзины, проверка что корзина пуста и текст о пустой корзине

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"  # Задаем основную ссылку (ссылка откроется после запуска браузера)
        page = BasketPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # Открываем страницу
        page.go_to_basket_page() # выполняем метод - переход в корзину заказов
        page.check_basket() # выполняем список метод - проверка открытия станицы корзины, проверка что корзина пуста и текст о пустой корзине