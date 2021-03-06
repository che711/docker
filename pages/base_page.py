from imghdr import what
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    def fird_and_click_button(self):
        self.browser.find_element(By.CSS_SELECTOR, what)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True



