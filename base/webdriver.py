import traceback
from selenium import webdriver


class WebDriver():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://www.google.com"
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
