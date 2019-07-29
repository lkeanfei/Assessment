
from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.quantityButtonDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.ID,
            MOBILEFINDTAGS.ANDROIDTAG : "com.zalora.android:id/product_quantity_button",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        self.goToCheckoutDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/checkout_button",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

    def getQuantity(self):

        elem = self.mobileDriver.getElement(self.quantityButtonDict)
        return elem.text

    def goToCheckout(self):

        self.mobileDriver.clickElement(self.goToCheckoutDict)

