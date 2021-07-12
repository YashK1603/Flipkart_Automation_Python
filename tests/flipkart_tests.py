import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.google_search_page import GoogleSearch
from pages.home.flipkart_home_page import FlipkartPage
from pages.home.compare_page import ComparePage
from pages.home.cart_page import CartPage
import pytest
import unittest
import time


@pytest.mark.usefixtures("oneTimeSetUp")
class Test_FlipkartFlow(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.gs = GoogleSearch(self.driver)
        self.fp = FlipkartPage(self.driver)
        self.cp = ComparePage(self.driver)
        self.cartp = CartPage(self.driver)

    # TestCases of GoogleSearch from google_search_page starts :
    @pytest.mark.run(order=1)
    def test_searchFlipkart(self):
        self.gs.enterSearchField("Flipkart")

    @pytest.mark.run(order=2)
    def test_getSearchSuggestions(self):
        self.gs.searchSuggestions()
        # assert check is pending

    @pytest.mark.run(order=3)
    def test_navigateToFlipkart(self):
        self.gs.goToFlipkart()
        # assert check is pending

    # TestCases of GoogleSearch from google_search_page ends :

    # TestCases of FlipkartHomepages from flipkart_home_page starts :
    @pytest.mark.run(order=4)
    def test_closeLoginPopup(self):
        self.fp.closeLoginPopup()

    @pytest.mark.run(order=5)
    def test_navigateToAC(self):
        self.fp.gotoWindowACs()

    @pytest.mark.run(order=6)
    def test_addToCompare(self):
        self.fp.addToCompare()

    # TestCases of FlipkartHomepages from flipkart_home_page ends :

    # TestCases of ComparePage from compare_page starts :
    @pytest.mark.run(order=7)
    def test_getNameAndPrice(self):
        self.cp.nameAndPrice()

    @pytest.mark.run(order=8)
    def test_test_itemsAddToCart(self):
        self.cp.addToCart()

    # TestCases of ComparePage from compare_page Ends :

    # TestCases of CartPage from cart_page starts :
    @pytest.mark.run(order=9)
    def test_checkdelpin(self):
        self.cartp.checkDeliveryPin(380015)

    @pytest.mark.run(order=10)
    def test_checkDiffDelPin(self):
        self.cartp.checkdiffdelpin(365601)
