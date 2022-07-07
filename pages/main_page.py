# Импортируем базовый класс BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
# Импорт класса с локаторами
from .locators import MainPageLocators
# Импорт класса LoginPage
from .login_page import LoginPage

# MainPage наследник BasePage (MainPage имеет полный доступ к всем атрибутам и методам класса-предка)
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # Возвращаем url страницы на которую перешли в результате клика
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        #символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "ссылка на логин отсутствует"