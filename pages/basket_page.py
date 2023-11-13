from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators

class BasketPage(BasePage):
    
    def should_be_basket__is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            'Empty basket message was not found'

    def should_be_no_product_added_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST_IN_BASKET), \
            'There are products found in basket, but it should be empty'