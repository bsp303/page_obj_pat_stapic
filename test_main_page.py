import time

from selenium.webdriver.common.by import By
# импорт каласа описывающего главную страницу
from .pages.main_page import MainPage
# испортируем LoginPage
from .pages.login_page import LoginPage

def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = LoginPage (browser, link) # инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    #открываем страницу
    time.sleep(2)
    page.should_be_login_page() # выполняем метод страницы - переходим на страницу логина