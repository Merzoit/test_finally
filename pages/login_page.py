from .base_page import BasePage
from .locators import LoginPageLocators 

class LoginPage(BasePage):
    def should_be_login_page(self):
        """ Tests for login page """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ Check 'login' in link """
        cur_url = self.browser.current_url
        lg = "login"
        assert lg in cur_url, 'Link error'
        

    def should_be_login_form(self):
        """ Check login form """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"
        

    def should_be_register_form(self):
        """ Check registration form """
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not present"
        