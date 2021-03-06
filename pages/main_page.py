from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
from .login_page import LoginPage


class MainPage(BasePage): 
    def should_be_login_link(self):
        """ Check login link presented """
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    
    def go_to_login_page(self):
        """ Go to the login page """
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()
        