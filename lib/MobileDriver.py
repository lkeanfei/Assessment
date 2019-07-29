

import copy

from enum import Enum
import logging

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys





class MOBILEOS(Enum):
    ANDROID = 1
    IOS = 2

class MOBILEFINDTAGS:

    ANDROIDBYTAG = "AndroidByTag"
    ANDROIDTAG = "AndroidTag"
    IOSBYTAG = "IosByTag"
    IOSTAG = "IosTag"

class MobileDriver:

    def __init__(self , mobileOS):

        self.mobileOS = mobileOS
        self.driver = None

        if self.mobileOS == 'Android':
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '8.1'
            desired_caps['automationName'] = 'uiautomator2'
            desired_caps['newCommandTimeout'] = 180
            desired_caps['deviceName'] = 'Galaxy Tab A'
            desired_caps['appPackage'] = 'com.zalora.android'
            desired_caps['appActivity'] = 'pt.rocket.view.activities.SplashScreenActivity'

            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        elif self.mobileOS == 'IOS':
            print('Not implemented')


        logging.getLogger().info("OS is " + mobileOS)

    def getAllContexts(self):

        return self.driver.contexts

    def getMobileOS(self):
        return self.mobileOS

    def getElement(self , elemDict , index = 1):

        if self.mobileOS == 'Android':
            byTag = elemDict[MOBILEFINDTAGS.ANDROIDBYTAG]
            tag = elemDict[MOBILEFINDTAGS.ANDROIDTAG]
        else:
            byTag = elemDict[MOBILEFINDTAGS.IOSBYTAG]
            tag = elemDict[MOBILEFINDTAGS.IOSTAG]

        elem = None

        logging.getLogger().info(str(elemDict))

        logging.getLogger().info( byTag  )
        logging.getLogger().info(tag)

        wait = WebDriverWait(self.driver,20)
        wait.until(EC.element_to_be_clickable((byTag, tag)))

        if index == 1:

            if byTag == By.ID:
                elem = self.driver.find_element_by_id(tag)
            elif byTag == By.XPATH:
                elem = self.driver.find_element_by_xpath(tag)
        else:

            if byTag == By.ID:
                elems = self.driver.find_elements_by_id(tag)
            elif byTag == By.XPATH:
                elems = self.driver.find_elements_by_xpath(tag)

            elem = elems[index]



        return elem



    def clickElement(self , elemDict , index = 1):

        if self.mobileOS == 'Android':
            byTag = elemDict[MOBILEFINDTAGS.ANDROIDBYTAG]
            tag = elemDict[MOBILEFINDTAGS.ANDROIDTAG]
        else:
            byTag = elemDict[MOBILEFINDTAGS.IOSBYTAG]
            tag = elemDict[MOBILEFINDTAGS.IOSTAG]

        elem = None

        # logging.getLogger().info(str(elemDict))
        #
        # logging.getLogger().info( byTag  )
        # logging.getLogger().info(tag)

        wait = WebDriverWait(self.driver,20)
        wait.until(EC.visibility_of_element_located((byTag, tag)))

        if index == 1:

            if byTag == By.ID:
                elem = self.driver.find_element_by_id(tag)
            elif byTag == By.XPATH:
                elem = self.driver.find_element_by_xpath(tag)
        else:

            if byTag == By.ID:
                elems = self.driver.find_elements_by_id(tag)
            elif byTag == By.XPATH:
                elems = self.driver.find_elements_by_xpath(tag)

            elem = elems[index]



        elem.click()

    def enterText(self, elemDict , text):

        if self.mobileOS == 'Android':
            byTag = elemDict[MOBILEFINDTAGS.ANDROIDBYTAG]
            tag = elemDict[MOBILEFINDTAGS.ANDROIDTAG]
        else:
            byTag = elemDict[MOBILEFINDTAGS.IOSBYTAG]
            tag = elemDict[MOBILEFINDTAGS.IOSTAG]

        elem = None

        logging.getLogger().info(str(elemDict))

        logging.getLogger().info(byTag)
        logging.getLogger().info(tag)

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((byTag, tag)))

        if byTag == By.ID:
            elem = self.driver.find_element_by_id(tag)
        elif byTag == By.XPATH:
            elem = self.driver.find_element_by_xpath(tag)

        elem.send_keys(text)

    def elementExists(self , elemDict):

        if self.mobileOS == 'Android':
            byTag = elemDict[MOBILEFINDTAGS.ANDROIDBYTAG]
            tag = elemDict[MOBILEFINDTAGS.ANDROIDTAG]
        else:
            byTag = elemDict[MOBILEFINDTAGS.IOSBYTAG]
            tag = elemDict[MOBILEFINDTAGS.IOSTAG]

        wait = WebDriverWait(self.driver, 25)
        wait.until(EC.element_to_be_clickable((byTag, tag)))


        elems = []
        if byTag == By.ID:
            elems = self.driver.find_elements_by_id(tag)
        elif byTag == By.XPATH:
            elems = self.driver.find_elements_by_xpath(tag)


        # logging.getLogger().info('Bytag ' + byTag + " : " + tag + " " + str(len(elems)))



        return len(elems) > 0












