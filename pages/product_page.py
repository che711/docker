from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_product(self):
        click_product = self.browser.find_element(*ProductPageLocators.FIRST_PRODUCT)
        click_product.click()

    def buy_first_product(self):
        buy_product = self.browser.find_element(*ProductPageLocators.BY_FIRST_PRODUCT)
        buy_product.click()
        # xpath_product = self. browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        # name_product = xpath_product.text

    def go_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.CART)
        basket.click()
        # xpath_product = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
        # name_product2 = xpath_product.text



