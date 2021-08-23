from selenium.webdriver.common.by import By

class CatalogPageLocators():
    CATALOG = (By.XPATH, '/html/body/div[1]/div/div/div/header/div[2]/div/nav/ul[1]/li[1]/a[2]/span')
    AVTO_MOTO = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/ul/li[7]')
    SOUND = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[6]/div[1]/div/div[5]')
    CABLES = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[3]/div/div[6]/div[1]/div/div[5]/div[2]/div/a[5]')

class ProductPageLocators():
    FIRST_PRODUCT = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div[4]/div[3]/div[4]/div[1]/div/div[3]/div[2]/div[1]/a/span")
    BY_FIRST_PRODUCT = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[1]/div/div/div/div[1]/a[3]')
    CART = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/main/div/div/aside/div[1]/div[1]/div/div/div/div[1]/a[3]')
    NAME_PRODUCT = (By.XPATH, "/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[4]/h1")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "a.cart-form__link_base-alter:nth-child(1)")

