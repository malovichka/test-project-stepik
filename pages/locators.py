from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.XPATH, '//a[contains(@href, "basket")]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_USERNAME = (By.ID, 'id_login-username')
    LOGIN_PASSWORD = (By.ID, 'id_login-password')
    LOGIN_PASSWORD_RESET_LINK = (By.XPATH, '//a[contains(@href, "password-reset")]')
    LOGIN_SUBMIT_BUTTON = (By.NAME, 'login_submit')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_CREATION = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD_CONFIRMATION = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.NAME, 'registration_submit')

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME_IN_BREADCRUMBS = (By.CSS_SELECTOR, '.breadcrumb > .active')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert-success:first-child > .alertinner > strong')
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert:last-child > .alertinner > p > strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_page .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert-success:first-child > .alertinner')


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
    PRODUCT_LIST_IN_BASKET = (By.ID, 'basket_formset')
    PRODUCT_LIST_IN_BASKET_INVALID = (By.CSS_SELECTOR, '#content_inner > p')