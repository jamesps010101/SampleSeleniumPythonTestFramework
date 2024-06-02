from base.base_page import BasePage
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators:
    _item_list = By.XPATH, "//div[@class='inventory_list']"
    _item_name = By.CLASS_NAME, "inventory_item_name "
    _item_price = By.CLASS_NAME, "inventory_item_price"
    _add_cart_button = By.XPATH, ".//button[starts-with(@id,'add-to-cart')]"
    _remove_cart_button = By.XPATH, ".//button[starts-with(@id,'remove-')]"
    _sort_dropdown = By.XPATH, "//select[@class='product_sort_container']"
    _sort_option_lohi = By.XPATH, "//option[@value='lohi']"

    # Dynamic Locators:
    _single_item_div = By.XPATH, "//div[@class='inventory_item_name ' and text()='{0}']/ancestor::div[@class='inventory_item']"

    # Methods (actions):
    def get_item_list(self):
        return self.do_find_element(self._item_list)

    def get_single_item(self, item_name):
        locator = self.build_locator(self._single_item_div, item_name)
        item_list = self.get_item_list()
        return self.do_find_element(locator, item_list)

    def get_first_item_name(self):
        return self.do_get_text(self._item_name)

    def get_item_price(self, item):
        item_price = self.do_find_element(self._item_price, item)
        return self.do_get_text(element=item_price)

    def click_add_cart_button(self, item):
        add_item_button = self.do_find_element(self._add_cart_button, item)
        self.do_click(element=add_item_button)

    def click_remove_cart_button(self, item):
        remove_item_button = self.do_find_element(self._remove_cart_button, item)
        self.do_click(element=remove_item_button)

    def verify_added_to_cart(self, item_name):
        item = self.get_single_item(item_name)
        remove_item_button = self.do_find_element(self._remove_cart_button, item)
        return remove_item_button is not None

    def verify_removed_from_cart(self, item_name):
        item = self.get_single_item(item_name)
        add_item_button = self.do_find_element(self._add_cart_button, item)
        return add_item_button is not  None

    def click_sort_low_to_high(self):
        self.do_click(self._sort_option_lohi)

    def click_item_link(self, item_name):
        item = self.get_single_item(item_name)
        item_link = self.do_find_element(self._item_name, item)
        self.do_click(element=item_link)
