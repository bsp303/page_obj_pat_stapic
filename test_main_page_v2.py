# Импорт рабочих методов
from .pages.main_page_v2 import MainPageV2
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page_v2(browser):
    link = "http://selenium1py.pythonanywhere.com"   # Присвоили значение переменной
    page = MainPageV2 (browser, link)    # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()    # Открываем страницу при помощи метода open что в base_page
    page.go_to_login_page_v2()    # Выполняем метод go_to_login_page_v2 из main_page_v2
    login_page = LoginPage(browser, browser.current_url)    # Присваиваем переменной значение
    login_page.should_be_login_page()    # Передаем в метод присвоенное значение
