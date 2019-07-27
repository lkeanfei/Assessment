from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By

class LanguageSelectionPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.languageSelectionDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.XPATH,
            MOBILEFINDTAGS.ANDROIDTAG : "//*[@resource-id='com.zalora.android:id/title' and @text='SELECT LANGUAGE']",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",

        }

        self.englishDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.XPATH,
            MOBILEFINDTAGS.ANDROIDTAG : "//*[@resource-id='com.zalora.android:id/splash_item_name' and @text='ENGLISH']",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",

        }


    def exists(self):

        return self.mobileDriver.elementExists(self.languageSelectionDict)

    def selectEnglish(self):

        return self.mobileDriver.clickElement(self.englishDict)