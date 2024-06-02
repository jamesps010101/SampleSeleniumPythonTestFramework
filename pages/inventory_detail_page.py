from base.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators:
    _back_to_products_button = By.ID, "back-to-products"
    _add_to_cart_button = By.ID, "add-to-cart"
    _remove_from_cart_button = By.ID, "remove"

    # Methods (actions):
    def verify_detail_page(self):
        return self.do_is_displayed(self._back_to_products_button)

    def click_add_to_cart_button(self):
        self.do_click(self._add_to_cart_button)

    def click_remove_from_cart_button(self):
        self.do_click(self._remove_from_cart_button)

    def verify_added_to_cart(self):
        return self.do_is_displayed(self._remove_from_cart_button)

    def verify_removed_from_cart(self):
        return self.do_is_displayed(self._add_to_cart_button)
    