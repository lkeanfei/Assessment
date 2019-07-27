
from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By

class ShopSelectionPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.shopSelectionDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.XPATH,
            MOBILEFINDTAGS.ANDROIDTAG : "//*[@resource-id='com.zalora.android:id/segment' and @text='SHOP MEN']",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",

        }

    def selectShopMen(self):

        self.mobileDriver.clickElement(self.shopSelectionDict)
