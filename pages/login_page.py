from base.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")

    # Locators:
    _page_header_text = By.XPATH, "//div[@class='login_logo']"
    _username_input = By.ID, "user-name"
    _password_input = By.ID, "password"
    _login_button = By.ID, "login-button"
    _login_error_text = By.XPATH, "//h3[@data-test='error']"
    _login_verify_text = By.XPATH, "//span[@class='title']"

    # Methods (actions):
    def get_page_header(self):
        return self.do_get_text(self._page_header_text)

    def enter_username_input(self, username):
        self.do_send_keys(self._username_input, username)

    def enter_password_input(self, password):
        self.do_send_keys(self._password_input, password)

    def click_login_button(self):
        self.do_click(self._login_button)

    def login(self, username, password):
        self.enter_username_input(username)
        self.enter_password_input(password)
        self.click_login_button()

    def get_error_login_text(self):
        return self.do_get_text(self._login_error_text)

    def verify_login(self):
        return self.do_get_text(self._login_verify_text) == "Products"

    def verify_logout(self):
        return self.do_is_displayed(self._username_input)
