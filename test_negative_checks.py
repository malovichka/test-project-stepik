from pages.product_page import ProductPage
import pytest

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.xfail(reason='it fails on purpose')
def test_guest_cannot_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cannot_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason='it fails on purpose')
def test_essage_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_message_disappear()



