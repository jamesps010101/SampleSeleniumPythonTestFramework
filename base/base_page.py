from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from utils.logger_util import logger_tool
import logging


class BasePage:
    log = logger_tool(log_level=logging.INFO)
    errors = [NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver=self.driver, timeout=3, poll_frequency=0.2, ignored_exceptions=self.errors)

    def do_find_element(self, locator, element: WebElement = None):
        found_element = None
        try:
            if element:
                found_element = element.find_element(*locator)
            else:
                found_element = self.wait.until(EC.presence_of_element_located(locator))
        except:
            self.log.error(f"find_element:element not found:locator={locator}")
        return found_element

    def do_find_elements(self, locator, element: WebElement = None):
        found_elements = None
        try:
            if element:
                found_elements = element.find_elements(*locator)
            else:
                found_elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        except:
            self.log.error(f"find_elements:elements not found:locator={locator}")
        return found_elements

    def do_send_keys(self, locator="", data="", element=None):
        try:
            if element:
                element.send_keys(data)
            else:
                find_element = self.do_find_element(locator)
                self.wait.until(EC.element_to_be_clickable(find_element)).send_keys(data)
        except:
            self.log.error(f"send_keys:failed:locator={locator}")

    def do_click(self, locator="", element=None):
        try:
            if not element:
                element = self.do_find_element(locator)
            self.wait.until(EC.element_to_be_clickable(element)).click()
        except:
            self.log.error(f"click:failed:locator={locator}")

    def do_get_text(self, locator="", element=None):
        text = None
        try:
            if not element:
                element = self.do_find_element(locator)
            text = element.text
        except:
            self.log.error(f"get_text:failed:locator={locator}")
        return text

    def do_is_displayed(self, locator):
        is_displayed = False
        try:
            element = self.do_find_element(locator)
            is_displayed = element.is_displayed()
        except:
            self.log.error(f"do_is_displayed:failed:locator={locator}")
        return is_displayed

    @staticmethod
    def build_locator(locator_list, text):
        by_type, locator = locator_list[0], locator_list[1].format(text)
        return by_type, locator
