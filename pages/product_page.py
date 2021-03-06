from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket_buttton(self):
        """ Add product to basket """
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def check_add_basket_text(self):
        """ Check added to basket text """
        txt = self.browser.find_element(*ProductPageLocators.ADD_TXT).text
        assert "has been" in txt, 'Added text not present'

    def check_name_coincidence(self):
        """ Check name coincidence """
        cur_block = self.browser.find_element(*ProductPageLocators.ADD_TXT)
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        cur_name = cur_block.find_element(*ProductPageLocators.PRODUCT_CUR_NAME).text
        assert name == cur_name, 'Product name not coincidence'

    def check_basket_info(self):
        """ Check basket info block and price coincidence """
        basket_info_block = self.browser.find_element(*ProductPageLocators.BASKET_INFO)
        assert basket_info_block, 'Basket info block not present'
        basket_total = basket_info_block.find_element(*ProductPageLocators.PRODUCT_CUR_NAME).text
        product_info_block = self.browser.find_element(*ProductPageLocators.PRODUCT_INFO)
        cur_price = product_info_block.find_element_by_tag_name('p').text
        print(basket_total + '1')
        print(cur_price + '2')
        assert basket_total == cur_price, 'Product price not coincidence'

   