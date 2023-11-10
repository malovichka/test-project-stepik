from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_promo_url(self):
        assert 'promo' in self.browser.current_url, \
            'Substring "promo" not found in URL'

    def should_be_added_to_basket(self):
        #right product was added
        product_in_catalogue = self.get_text(*ProductPageLocators.PRODUCT_NAME_IN_BREADCRUMBS)
        product_in_basket = self.get_text(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)       
        assert product_in_catalogue == product_in_basket, \
            f'Added "{product_in_catalogue}" to basket, got "{product_in_basket}" in message instead'

    def should_be_basket_price(self):
        #message with basket total price
        price_of_product = self.get_text(*ProductPageLocators.PRODUCT_PRICE)
        basket_price_in_message = self.get_text(*ProductPageLocators.BASKET_TOTAL_MESSAGE)
        assert price_of_product == basket_price_in_message, \
            f'Expected "{price_of_product}", got "{basket_price_in_message}" in message instead'
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message is presented, but it should not be'
        
    def should_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Message still present, but it should dissappear'
        
    def should_be_removed_product(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_IN_BASKET), \
            'Product still present, but it should dissappear'
        

    