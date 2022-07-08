# испортируем класс MainPage из файла main_page.py
from .pages.main_page_v1 import MainPageV1

def test_guest_can_go_to_login_page_v1(browser):
    link = "http://selenium1py.pythonanywhere.com/"    # Задаем первоначальную ссылку
    page = MainPageV1(browser, link)    # Инициализация Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()     # Открываем страницу при помощи метода open что в base_page
    login_page = page.go_to_login_page_v1()    # Сохраняем в переменную login_page результат go_to_login_page_v1 (url)
    login_page.should_be_login_page()    # Передаем полуенный результат на проверки в методе should_be_login_page
