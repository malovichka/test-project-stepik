import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action = 'store',
                     default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--user_language',
                     action = 'store',
                     default = 'en',
                     help = 'Choose language: ru, en, etc.')


@pytest.fixture(scope='function')
def browser(request) -> webdriver.Chrome:
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('user_language')
    browser = None
    if browser_name == 'chrome':
        print('\nstart browser for testing...')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', 
                                               {'intl.accept_languages': user_language})
        chrome_options.add_argument('--incognito')
        browser = webdriver.Chrome(options=chrome_options)
        browser.implicitly_wait(1)
    elif browser_name == 'firefox':
        print('\nstart browser for testing...')
        ff_options = webdriver.FirefoxOptions()
        ff_options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=ff_options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nquit browser...')
    browser.quit()
