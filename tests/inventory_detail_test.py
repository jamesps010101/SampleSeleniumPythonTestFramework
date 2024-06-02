import unittest

import pytest
from pages.inventory_detail_page import InventoryDetailPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("class_setup_teardown")
class InventoryDetailTest(unittest.TestCase):
    @pytest.fixture(autouse=True, scope="class")
    def class_setup(self, class_setup_teardown):
        self.lp = LoginPage(self.driver)
        self.lp.login("standard_user", "secret_sauce")

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ip = InventoryPage(self.driver)
        self.idp = InventoryDetailPage(self.driver)

    @pytest.mark.run(order=8)
    def test_detail_page_loaded(self):
        item_name = "Sauce Labs Onesie"
        self.ip.click_item_link(item_name)
        result = self.idp.verify_detail_page()
        assert result is True, "Detail page not loaded correctly"

    @pytest.mark.run(order=9)
    def test_add_to_cart(self):
        self.idp.click_add_to_cart_button()
        result = self.idp.verify_added_to_cart()
        assert result is True, "Add to cart failed"

    @pytest.mark.run(order=10)
    def test_remove_from_cart(self):
        self.idp.click_remove_from_cart_button()
        result = self.idp.verify_removed_from_cart()
        assert result is True, "Remove from cart failed"
