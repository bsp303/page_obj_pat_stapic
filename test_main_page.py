import time
# испортируем класс LoginPage из файла login_page.py
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage



def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/" # Задаем основную ссылку (ссылка откроется после запуска браузера)
    page = LoginPage(browser, link) # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    # Открываем страницу
    time.sleep(2)
    page.should_be_login_page() # выполняем метод страницы - переходим на страницу логина

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.check_basket()