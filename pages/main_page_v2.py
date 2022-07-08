# Импортируем базовый локаторы
from .base_page import BasePage
from .locators import MainPageLocators



class MainPageV2(BasePage):
    # Переход по тапу на локатор
    def go_to_login_page_v2(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)    # Присваиваем переменной локатор
        link.click()    # Выполняем клик по локатору
