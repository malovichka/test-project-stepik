from pages.product_page import ProductPage
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_url()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(600)
    # page.should_be_added_to_basket()
    # page.should_be_basket_price()


