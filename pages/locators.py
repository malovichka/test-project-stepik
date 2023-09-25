from selenium.webdriver.common.by import By

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
        