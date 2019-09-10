from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_name()
        self.should_be_price()
        self.should_be_add_to_basket_button()

    def should_be_promo_new_year_url(self):
        assert '?promo=newYear' in self.browser.current_url, "'?promo=newYear' not in url"

    def should_be_name(self):
        assert self.is_element_present(*ProductPageLocators.NAME_SHOWED), "Product name in desc is not presented"

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_SHOWED), "Product price in desc is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON),\
            "Add to basket button is not presented"

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_message_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE),\
            "Product price in message is not presented"

    def should_be_message_name(self):
        assert self.is_element_present(*ProductPageLocators.NAME_MESSAGE), "Name in message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_MESSAGE), \
            "Success message is not disappeared"

    def get_showed_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_SHOWED).text

    def get_showed_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_SHOWED).text

    def get_message_name(self):
        self.should_be_message_name()
        return self.browser.find_element(*ProductPageLocators.NAME_MESSAGE).text

    def get_message_basket_total(self):
        self.should_be_message_basket_total()
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

    def check_equal_price(self, message_price):
        price = self.get_showed_price()
        assert message_price == price, 'Wrong price in message'

    def check_equal_name(self, message_name):
        name = self.get_showed_name()
        assert message_name == name, 'Wrong name in message'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_MESSAGE), \
            "Success message not disappear"
