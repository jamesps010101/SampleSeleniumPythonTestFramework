import unittest

import pytest
from pages.login_page import LoginPage
from pages.menu_header_page import MenuHeaderPage


@pytest.mark.usefixtures("class_setup_teardown")
class LoginTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, class_setup_teardown):
        self.lp = LoginPage(self.driver)
        self.mhp = MenuHeaderPage(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        username = "aaaa"
        password = "bbbb"
        expected_text = "Epic sadface: Username and password do not match any user in this service"

        self.lp.login(username, password)
        actual_text = self.lp.get_error_login_text()

        assert actual_text == expected_text, "Invalid login did not produce correct error"

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        username = "standard_user"
        password = "secret_sauce"
        expected_result = True

        self.lp.login(username, password)
        actual_result = self.lp.verify_login()

        assert actual_result is expected_result, "Valid login failed"

    @pytest.mark.run(order=3)
    def test_logout(self):
        username = "standard_user"
        password = "secret_sauce"
        self.lp.login(username, password)
        self.mhp.click_menu_button()
        self.mhp.click_logout_button()
        result = self.lp.verify_logout()
        assert result is True, "Logout failed"
