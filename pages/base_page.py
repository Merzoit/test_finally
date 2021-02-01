from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        """ Initialization  """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self): 
        """ Open browser with current URL """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """ Check element presentation """
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True

    