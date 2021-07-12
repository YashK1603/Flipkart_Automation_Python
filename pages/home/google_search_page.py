import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class GoogleSearch(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_field = "//input[@title='Search']"
    _search_suggestions = ".//ul[@role='listbox']/li//div[contains(@class, 'wM6W7d')]/span"
    _flipkart_link = ".//a[@href='https://www.flipkart.com/']//h3[text()='Flipkart']"

    def enterSearchField(self, searchgoogle):
        self.sendKeys(searchgoogle, self._search_field, locatorType="xpath")
        time.sleep(1)

    def searchSuggestions(self):
        suggestionlists = self.driver.find_elements(By.XPATH, self._search_suggestions)

        print("\n\bThe google suggestions are as below: ")
        for lists in suggestionlists:
            print(lists.text)
        self.elementClick(self._search_suggestions, locatorType="xpath")
        time.sleep(1)

    def goToFlipkart(self):
        self.elementClick(self._flipkart_link, locatorType="xpath")
