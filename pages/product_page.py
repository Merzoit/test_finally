from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket_buttton(self):
        """ Add product to basket """
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    