import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="chrome", help="Choose browser: 'ru' or 'en-bg")

@pytest.fixture(scope="function")
def browser(request):
    # обявляем переменную в которую будем писать название браузера
    language = request.config.getoption("language")
    br_lang = language
    if language == br_lang:
        print("\nзапуск  браузера")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("в переменноц language отсутствует значение")
    yield browser
    print("\n... закрытие браузера")
    browser.quit()