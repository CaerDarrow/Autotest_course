from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    NAME_SHOWED = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_SHOWED = (By.CSS_SELECTOR, '.product_main p')
    NAME_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(3) strong')
    BASKET_TOTAL_HEADER = (By.CSS_SELECTOR, '.basket-mini strong')

