import unittest

import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("class_setup_teardown")
class InventoryTest(unittest.TestCase):
    @pytest.fixture(autouse=True, scope="class")
    def class_setup(self, class_setup_teardown):
        self.lp = LoginPage(self.driver)
        self.lp.login("standard_user", "secret_sauce")

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ip = InventoryPage(self.driver)

    @pytest.mark.run(order=4)
    def test_item_found(self):
        item_name = "Sauce Labs Fleece Jacket"
        item = self.ip.get_single_item(item_name)
        if item:
            item_price = self.ip.get_item_price(item)

            assert item_price == "$49.99"
        else:
            assert False

    @pytest.mark.run(order=5)
    def test_add_to_cart(self):
        item_name = "Sauce Labs Fleece Jacket"
        item = self.ip.get_single_item(item_name)
        if item:
            self.ip.click_add_cart_button(item)
            result = self.ip.verify_added_to_cart(item_name)
            assert result is True, "Failed to add to cart"
        else:
            assert False

    @pytest.mark.run(order=6)
    def test_remove_from_cart(self):
        item_name = "Sauce Labs Fleece Jacket"
        item = self.ip.get_single_item(item_name)
        if item:
            self.ip.click_remove_cart_button(item)
            result = self.ip.verify_removed_from_cart(item_name)
            assert result is True, "Failed to remove from cart"
        else:
            assert False

    @pytest.mark.run(order=7)
    def test_sort(self):
        expected_name = "Sauce Labs Onesie"
        self.ip.click_sort_low_to_high()
        actual_name = self.ip.get_first_item_name()
        assert actual_name == expected_name, "Sort failed"
