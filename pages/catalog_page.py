from .base_page import BasePage
from .locators import CatalogPageLocators

class CatalogPage(BasePage):

    def go_catalog(self):
        clic_catalog = self.browser.find_element(*CatalogPageLocators.CATALOG)
        clic_catalog.click()

    def go_to_avtomoto(self):
        clic_avto = self.browser.find_element(*CatalogPageLocators.AVTO_MOTO)
        clic_avto.click()

    def go_to_sound(self):
        clic_sound = self.browser.find_element(*CatalogPageLocators.SOUND)
        clic_sound.click()

    def go_to_cable(self):
        clic_cable = self.browser.find_element(*CatalogPageLocators.CABLES)
        clic_cable.click()

