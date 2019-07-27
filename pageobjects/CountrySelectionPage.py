from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By

class CountrySelectionPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.countrySelectionDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.XPATH,
            MOBILEFINDTAGS.ANDROIDTAG : "//*[@resource-id='com.zalora.android:id/title' and @text='SELECT LOCATION']",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",

        }

        self.malaysiaDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.XPATH,
            MOBILEFINDTAGS.ANDROIDTAG : "//*[@resource-id='com.zalora.android:id/splash_item_name' and @text='MALAYSIA']",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",

        }


    def exists(self):

        return self.mobileDriver.elementExists(self.countrySelectionDict)

    def selectCountry(self , countryName):

        self.malaysiaDict[MOBILEFINDTAGS.ANDROIDTAG] = "//*[@resource-id='com.zalora.android:id/splash_item_name' and @text='" + countryName +"']"

        return self.mobileDriver.clickElement(self.malaysiaDict)


