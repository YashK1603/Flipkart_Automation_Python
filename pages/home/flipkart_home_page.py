import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.seleniumdriver import SeleniumDriver
from selenium.webdriver import ActionChains
import utilities.custom_logger as cl
import logging
import time


class FlipkartPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _closePopup = "_2doB4z"
    _appliances = "img[alt='Appliances']"
    _airConditioners = "Air Conditioners"
    _windowACs = "Window ACs"
    _addToCompare_2 = "//div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[2]//span[.='Add to Compare']"
    _addToCompare_3 = "//div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[4]//span[.='Add to Compare']"
    _addToCompare_6 = "//div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[7]//span[.='Add to Compare']"
    _comparebtn = "//span[@class='_3hShhO']/span[.='COMPARE']"

    def closeLoginPopup(self):
        self.elementClick(self._closePopup, locatorType="class")

    def gotoWindowACs(self):
        actions = ActionChains(self.driver)
        applianceElement = self.getElement(self._appliances, locatorType="css")
        actions.move_to_element(applianceElement).perform()

        airConditionerElement = self.getElement(self._airConditioners, locatorType="link")
        actions.move_to_element(airConditionerElement).perform()

        self.elementClick(self._windowACs, locatorType="link")

    def addToCompare(self):
        self.elementClick(self._addToCompare_2, locatorType="xpath")
        self.elementClick(self._addToCompare_3, locatorType="xpath")
        self.elementClick(self._addToCompare_6, locatorType="xpath")

        self.elementClick(self._comparebtn, locatorType="xpath")


