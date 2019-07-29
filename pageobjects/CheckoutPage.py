
from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.continueToPaymentDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.ID,
            MOBILEFINDTAGS.ANDROIDTAG : "saveAndContinue",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

    def continuePaymentMode(self):

        contextList = self.mobileDriver.getAllContexts()

        assert "WEBVIEW" in contextList, "WEBVIEW context is not available in Checkout Page. Available contexts are " + ",".join(
            contextList)

        self.mobileDriver.clickElement(self.continueToPaymentDict)

