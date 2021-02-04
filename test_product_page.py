from selenium import webdriver
from test_finally.pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    """ Test-case """
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket_buttton()
    product_page.solve_quiz_and_get_code()
    product_page.check_add_basket_text()
    product_page.check_name_coincidence()
    product_page.check_basket_info()