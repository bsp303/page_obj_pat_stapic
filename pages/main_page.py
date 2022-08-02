from .base_page import BasePage

# MainPage наследник BasePage (MainPage имеет полный доступ к всем атрибутам и методам класса-предка)
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)