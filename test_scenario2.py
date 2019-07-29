# coding=utf-8
"""Blog feature tests."""


from lib.MobileDriver import MobileDriver
from pageobjects import CountrySelectionPage
from pageobjects import LanguageSelectionPage
from pageobjects import LoginPage
from pageobjects import ShopSelectionPage , TutorialPage , CatalogPage , CartPage , CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait

import logging
import datetime
from time import mktime

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('test_scenario2.feature', 'Order Transaction')
def test_Scenario2_OrderTransaction(mobileDriver: MobileDriver):
    print('step 1')



@given('that Country and Language Selection has completed')
def completeCountryAndLanguageSelection(mobileDriver: MobileDriver):
    """Sets up """
    countrySelectionPage = CountrySelectionPage.CountrySelectionPage(mobileDriver)
    assert countrySelectionPage.exists() , "Country selection page does not exist"
    countrySelectionPage.selectCountry("MALAYSIA")

    languageSelectionPage = LanguageSelectionPage.LanguageSelectionPage(mobileDriver)
    assert languageSelectionPage.exists(), "Language selection page does not exist"
    languageSelectionPage.selectEnglish()

    loginPage = LoginPage.LoginPage(mobileDriver)
    assert loginPage.exists() , "Login page does not exist"

    loginPage.enterUserName()
    loginPage.enterPassword()
    loginPage.clickLoginButton()





@when('I select and add product to cart')
def selectAndAddProductToCart( mobileDriver: MobileDriver):
    """Post to Login handler"""
    shopSelectionPage = ShopSelectionPage.ShopSelectionPage(mobileDriver)
    shopSelectionPage.selectShopMen()

    tutorialPage = TutorialPage.TutorialPage(mobileDriver)
    tutorialPage.skip()

    catalogPage = CatalogPage.CatalogPage(mobileDriver)
    catalogPage.selectImageCampaign()
    catalogPage.selectFirstProduct()
    catalogPage.clickOnPrice()
    catalogPage.selectLSize()
    catalogPage.addToBag()
    catalogPage.clickCartButton()

    cartPage = CartPage.CartPage(mobileDriver)
    strActualQuantity = cartPage.getQuantity()
    actualQuantity = int(strActualQuantity)
    assert actualQuantity > 0, "Expected the quantity to be more than 0. Actual is " + actualQuantity

    cartPage.goToCheckout()




@then('I should be able to checkout successfully')
def shouldBeAbleToCheckout( mobileDriver: MobileDriver):
    """I should not see the error message."""

    checkoutPage = CheckoutPage.CheckoutPage(mobileDriver)
    # checkoutPage.continuePaymentMode()



    print("")
