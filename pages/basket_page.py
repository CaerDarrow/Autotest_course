from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty(self):
        self.should_be_empty_text()
        self.should_not_be_goods()

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_EMPTY), "Text is not presented"

    def should_not_be_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS), "Goods is presented but should not"
