from .base_page import BasePage
from .locators import LoginPegeLocators

class LoginPage(BasePage):
    # метод запускающий все проверки последовательно
    def should_be_login_page(self):
        self.go_to_login_page()
        self.should_be_login_url()
        self.should_be_login_from()
        self.should_be_register_from()

    # переход на страницу авторизации
    def go_to_login_page(self):
        link = self.browser.find_element(*LoginPegeLocators.LOGIN_URL)
        link.click()
        # проверка наличия слова "login" в текущей ссылке
        assert "login" in self.browser.current_url, "ссылка на логин отсутствует"
        print("Выполнен переход на страницу регистации/авторизации")

    # проверка наличия ссылки для переходя на страницу авторизации/регистранции
    def should_be_login_url(self):
        link = self.browser.find_element(*LoginPegeLocators.LOGIN_URL)
        # проверка наличия слова "login" в текущей ссылке
        assert self.is_element_present(*LoginPegeLocators.LOGIN_URL), "ссылка на логин отсутствует"
        print("Ссылка на страницу регистации/авторизации отображена")

    # проверка наличия кнопки для авторизации
    def should_be_login_from(self):
        assert self.is_element_present(*LoginPegeLocators.BUTTON_LOGIN), "ссылка на кнопку Войти отсутствует"
        print("Кнопка для авторизации отображена")

    # проверка наличия кнопки для регистрации
    def should_be_register_from(self):
        assert self.is_element_present(*LoginPegeLocators.BUTTON_REGISTER), "ссылка на кнопку зарегистрироваться отсутствует"
        print("кнопка для регистрации отображена")

    # метод запускающий регистрацию нового клиента
    def registr_new_user(self, email, password):
        self.browser.find_element(*LoginPegeLocators.EMAIL_IMPUT).send_keys(email)
        self.browser.find_element(*LoginPegeLocators.PASS_REG_IMPUT1).send_keys(password)
        self.browser.find_element(*LoginPegeLocators.PASS_REG_IMPUT2).send_keys(password)
        self.browser.find_element(*LoginPegeLocators.REG_SUBMIT).click()
