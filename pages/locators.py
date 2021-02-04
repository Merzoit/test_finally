from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form') 
    REG_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CLASS_NAME, 'btn-lg')
    ADD_TXT = (By.CLASS_NAME, 'alertinner')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_CUR_NAME = (By.TAG_NAME, 'strong')
    BASKET_INFO = (By.CLASS_NAME, 'alert-info')
    PRODUCT_INFO = (By.CLASS_NAME, 'product_main')
    