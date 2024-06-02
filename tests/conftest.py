import pytest
import os
import datetime
from base.webdriver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope='class')
def class_setup_teardown(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = driver
    yield "class_setup_teardown"
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    reports_path = "C:\\users\\james\\workspace_python\\SeleniumTestFrameworkPython\\reports"
    report_file_name = f"{reports_path}\\{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.html"
    if not os.path.exists(reports_path):
        os.makedirs(reports_path)
    config.option.htmlpath = report_file_name
