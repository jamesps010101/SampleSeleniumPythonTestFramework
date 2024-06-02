from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "edge":
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()

        return driver
    