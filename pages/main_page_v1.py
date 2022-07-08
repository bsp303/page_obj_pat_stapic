# Импорт базового класа BasePage
from .base_page import BasePage
# Импорт класса с локаторами
from .locators import MainPageLocators
# Импорт класса с LoginPage
from .login_page import LoginPage

class MainPageV1(BasePage):
    # Измененние url полученный выполнения каких-то действий
    def go_to_login_page_v1(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)    # Сохраняем селектор в переменную
        link.click()    # Кликаем селектор
        return LoginPage(browser=self.browser, url=self.browser.current_url)    # Возвращаем текущую ссылку