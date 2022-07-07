from .base_page import BasePage
from .locators import LoginPegeLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_from()
        self.should_be_register_from()

    def should_be_login_url(self):
        link = self.browser.find_element(*LoginPegeLocators.LOGIN_URL)
        link.click()
        # проверка наличия слова "login" в текущей ссылке
        assert "login" in self.browser.current_url, "ссылка на логин отсутствует"
        print("проверка 1")

    def should_be_login_from(self):
        assert self.is_element_present(*LoginPegeLocators.BUTTON_LOGIN), "ссылка на кнопку Войти отсутствует"
        print("проверка 2")

    def should_be_register_from(self):
        assert self.is_element_present(*LoginPegeLocators.BUTTON_REGISTER), "ссылка на кнопку зарегистрироваться отсутствует"
        print("проверка 3")