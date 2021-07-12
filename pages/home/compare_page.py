import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class ComparePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _namesOfACs = ".//div[@class='_2d0DHb']//div[@class='row']//a"
    _pricesOfACs = "//div[@class='col-4-5']/div[2]//div[@class='_30jeq3']"
    _addToCart_1 = "//div[@class='_2eCJrS']//div[2]/button[@class='_2KpZ6l _2U9uOA _3v1-ww vsi37q']"
    _addToCart_2 = "//div[@class='_2eCJrS']//div[3]/button[@class='_2KpZ6l _2U9uOA _3v1-ww vsi37q']"
    _addToCart_3 = "//div[@class='_2eCJrS']//div[4]/button[@class='_2KpZ6l _2U9uOA _3v1-ww vsi37q']"
    _goToCart = ".//a[@class='_3SkBxJ']"

    def nameAndPrice(self):
        NamesOfACs = self.getElements(self._namesOfACs, locatorType="xpath")
        PricesOfACS = self.getElements(self._pricesOfACs, locatorType="xpath")

        print("\nNames of Windows ACs are as below: ")
        for names in NamesOfACs:
            print(names.text)

        print("\nPrices of Windows ACs are as below: ")
        for prices in PricesOfACS:
            print(" " + prices.text)

    def addToCart(self):

        self.elementClick(self._addToCart_1, locatorType="xpath")
        time.sleep(2)
        self.driver.back()

        self.elementClick(self._addToCart_2, locatorType="xpath")
        time.sleep(2)
        self.driver.back()

        self.elementClick(self._addToCart_3, locatorType="xpath")
        time.sleep(1)
