import time
from .pages.catalog_page import CatalogPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

# pytest -s -v test_base_page.py

def test_product_from_onliner(browser):
    link = "http://www.onliner.by/"
    page = CatalogPage(browser, link)
    page.open()
    page.go_catalog()
    page.go_to_avtomoto()
    page.go_to_sound()
    page.go_to_cable()
    page = ProductPage(browser, link)
    page.click_product()
    page.buy_first_product()
    xpath_product = browser.find_element(*ProductPageLocators.NAME_PRODUCT)
    name_product = xpath_product.text
    print(f"\n\tYou add to basket: {name_product}")
    time.sleep(1)
    page.go_basket()
    xpath_product = browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET)
    name_product2 = xpath_product.text
    print(f"\n\tProduct in basket: {name_product2}")
    correct_name = f"Кабель {name_product2}"
    assert (name_product == correct_name), "Product not founf"





