from base.base_page import BasePage
from selenium.webdriver.common.by import By


class MenuHeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators:
    _menu_button = By.ID, "react-burger-menu-btn"
    _logout_button = By.ID, "logout_sidebar_link"
    _cart_button = By.ID, "shopping_cart_container"

    # Methods (actions):
    def click_menu_button(self):
        self.do_click(self._menu_button)

    def click_cart_button(self):
        self.do_click(self._cart_button)

    def click_logout_button(self):
        self.do_click(self._logout_button)
