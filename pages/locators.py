from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPegeLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[name='login_submit']")
    BUTTON_REGISTER =(By.CSS_SELECTOR, "button[name='registration_submit']")