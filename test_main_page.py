from selenium.webdriver.common.by import By
# импорт каласа описывающего главную страницу
from .pages.main_page import MainPage

def test_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()    #открываем страницу
    #page.go_to_login_page()    # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_link() # выполнение метода провкрки ссылки на логин