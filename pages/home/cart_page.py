import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumdriver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class CartPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _searchPinCodeField = ".//input[ @class ='cfnctZ']"
    _checkPinCodeBtn = ".//div[@class='ibtBU6 _3t6eWY']/span"
    _checkDiffPinBtn = ".//div[@class='_1klldK']//span"
    _deliverystatus = ".//div[@class='_2pqhhf']"
    _deliverToField = "._12cXX4"

    def checkDeliveryPin(self, Pincode):
        self.sendKeys(Pincode, self._searchPinCodeField, locatorType="xpath")
        self.elementClick(self._checkPinCodeBtn, locatorType="xpath")
        time.sleep(2)

        DeliveryStatus = self.getElements(self._deliverystatus, locatorType="xpath")

        print("\nDelivery status of the products for Pincode " + str(Pincode) + " are as below: ")
        for status in DeliveryStatus:
            print(" " + status.text)
            # print(DelStatus.encode("utf-8"))

    def checkdiffdelpin(self, Pincode):
        self.elementClick(self._deliverToField, locatorType="css")

        self.sendKeys(Pincode, self._searchPinCodeField, locatorType="xpath")
        self.elementClick(self._checkDiffPinBtn, locatorType="xpath")
        time.sleep(2)

        DeliveryStatus = self.getElements(self._deliverystatus.encode("utf-8"), locatorType="xpath")

        print("\nDelivery status of the products for Pincode " + str(Pincode) + " are as below: ")
        for status in DeliveryStatus:
            print(" " + status.text)
