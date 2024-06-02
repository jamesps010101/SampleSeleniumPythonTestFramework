import unittest

import pytest
from pages.cart_checkout_page import CartCheckoutPage
from pages.menu_header_page import MenuHeaderPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("class_setup_teardown")
class CartCheckoutTest(unittest.TestCase):
    @pytest.fixture(autouse=True, scope="class")
    def class_setup(self, class_setup_teardown):
        self.lp = LoginPage(self.driver)
        self.lp.login("standard_user", "secret_sauce")

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ip = InventoryPage(self.driver)
        self.mhp = MenuHeaderPage(self.driver)
        self.ccp = CartCheckoutPage(self.driver)

    @pytest.mark.run(order=11)
    def test_checkout_process(self):
        item_name = "Sauce Labs Fleece Jacket"
        first_name = "John"
        last_name = "Doe"
        zip_code = "12345"

        item = self.ip.get_single_item(item_name)
        self.ip.click_add_cart_button(item)
        self.mhp.click_cart_button()
        self.ccp.checkout_process(first_name, last_name, zip_code)

        result = self.ccp.verify_order_checkout()

        assert result is True, "Checkout process failed"
