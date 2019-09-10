from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "'login' not in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_inp = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_inp.send_keys(email)
        pass_inp1 = self.browser.find_element(*LoginPageLocators.REG_PAS1)
        pass_inp1.send_keys(password)
        pass_inp2 = self.browser.find_element(*LoginPageLocators.REG_PAS2)
        pass_inp2.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON)
        submit_button.click()