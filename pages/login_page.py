from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, \
            'Substring "login" not found in URL'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), \
            'Login_username field was not found'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            'Login_password field was not found'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_RESET_LINK), \
            'Password reset link was not found'
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), \
            'Login_submit button was not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), \
            'Registration_email field was not found'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CREATION), \
            'Registration_password_creation field was not found'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION), \
            'Registration_password_confirmation field was not found'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), \
            'Registration_submit_button was not found'
        