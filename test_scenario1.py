# coding=utf-8
"""Blog feature tests."""


from lib.MobileDriver import MobileDriver
from pageobjects import CountrySelectionPage
from pageobjects import LanguageSelectionPage
from pageobjects import LoginPage
from pageobjects import ShopSelectionPage , TutorialPage , CatalogPage , CartPage
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

@scenario('test_scenario1.feature', 'Facebook Login')
def test_Scenario1_FacebookLogin(mobileDriver: MobileDriver):
    print('step 1')



@given('the Zalora App has completed Country and Language selection')
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



@when('I login with Facebook')
def loginToFacebook( mobileDriver: MobileDriver):
    """Post to Login handler"""
    loginPage = LoginPage.LoginPage(mobileDriver)
    loginPage.clickLoginToFacebook()
    loginPage.facebookLoginFormExists()




@then('I should see language selection page')
def shouldSeeLanguageSelectionPage( mobileDriver: MobileDriver):
    """I should not see the error message."""



    print("")
