from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPegeLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "button[name='login_submit']")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_CART_1 = (By.CSS_SELECTOR, "button[class='btn btn-lg btn-primary btn-add-to-basket']")
    BUTTON_ADD_TO_CART_2 = (By.CSS_SELECTOR, "#add_to_basket_form")
    BUTTON_ADD_TO_CART_3 = (By.XPATH, "//form[@id='add_to_basket_form']")
    TITLE_BOOK_MARKET = (By.XPATH, "//div/h1")
    TITLE_BOOK_ALLERT = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in'][1]//strong")
    PRICE_BOOK_MARKET = (By.XPATH, "//p[@class='price_color']")
    PRICE_BOOK_CART = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-info  fade in']//strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID =(By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    TITLE_BASKET_PAGE = (By.CSS_SELECTOR, ".page-header")
    MASSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p>a")
    BLOCK_THE_PRODUCTS =(By.CSS_SELECTOR, ".basket-title>div.row")