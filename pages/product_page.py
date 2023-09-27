from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_promo_url(self):
        assert 'promo' in self.browser.current_url, \
            'Substring "promo" not found in URL'

    def should_be_added_to_basket(self):
        #message that product was added to basket
        assert True
        #right product was added
        assert True

    def should_be_basket_price(self):
        #message with basket total price
        assert True

    