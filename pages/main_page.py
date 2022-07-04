# Импортируем базовый класс BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By

# MainPage наследник BasePage (MainPage имеет полный доступ к всем атрибутам и методам класса-предка)
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "ссылка на логин отсутствует"