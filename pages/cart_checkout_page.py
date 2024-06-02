from base.base_page import BasePage
from selenium.webdriver.common.by import By


class CartCheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators:
    _checkout_button = By.ID, "checkout"
    _firstname_input = By.ID, "first-name"
    _lastname_input = By.ID, "last-name"
    _zipcode_input = By.ID, "postal-code"
    _continue_button = By.ID, "continue"
    _finish_button = By.ID, "finish"
    _order_confirm_text = By.XPATH, "//h2[@class='complete-header']"

    # Methods (actions):
    def click_checkout_button(self):
        self.do_click(self._checkout_button)

    def enter_firstname(self, firstname):
        self.do_send_keys(self._firstname_input, firstname)

    def enter_lastname(self, lastname):
        self.do_send_keys(self._lastname_input, lastname)

    def enter_zipcode(self, zipcode):
        self.do_send_keys(self._zipcode_input, zipcode)

    def click_continue_button(self):
        self.do_click(self._continue_button)

    def click_finish_button(self):
        self.do_click(self._finish_button)

    def checkout_process(self, firstname, lastname, zipcode):
        self.click_checkout_button()
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_zipcode(zipcode)
        self.click_continue_button()
        self.click_finish_button()

    def verify_order_checkout(self):
        return self.do_get_text(self._order_confirm_text) == "Thank you for your order!"
    