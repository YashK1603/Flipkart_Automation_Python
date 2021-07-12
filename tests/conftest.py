import pytest
from selenium import webdriver
from base.webdriver import WebDriver


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    # Creating driver instance in oneTimeSetup as it will need to be execute once before starting tests
    wd = WebDriver(browser)
    driver = wd.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    # returning driver here so that it can be quit after all tests are executed using yield.
    yield driver

    # Closing browser after all tests are run
    driver.quit()

# Providing a way to access command line option while running the tests
def pytest_addoption(parser):
    parser.addoption("--browser")


# Creating python fixture for scope session
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
