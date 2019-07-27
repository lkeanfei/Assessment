
from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By
#
# firstProduct = driver.find_element_by_id('com.zalora.android:id/image_view')
# firstProduct.click()
#
# #Click on the price
# wait.until(EC.element_to_be_clickable((By.ID,"com.zalora.android:id/tv_pdv_product_special_price")))
# priceElement = driver.find_element_by_id('com.zalora.android:id/tv_pdv_product_special_price')
# priceElement.click()
#
# # 	com.zalora.android:id/iv_bubble_bg
# wait.until(EC.element_to_be_clickable((By.ID,"com.zalora.android:id/iv_bubble_bg")))
# sizeElements = driver.find_elements_by_id('com.zalora.android:id/iv_bubble_bg')
# sizeElements[2].click()
#
# addToBag = driver.find_element_by_id("com.zalora.android:id/layout_add_to_bag")
# addToBag.click()
#
# cartButton = driver.find_element_by_id("com.zalora.android:id/cart_button")
# cartButton.click()

class CatalogPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.imageCampaignDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.ID,
            MOBILEFINDTAGS.ANDROIDTAG : 'com.zalora.android:id/img_campaign',
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        # 'com.zalora.android:id/image_view'
        self.firstProductDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: 'com.zalora.android:id/image_view',
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }
        # 'com.zalora.android:id/tv_pdv_product_special_price'
        self.priceDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG:  'com.zalora.android:id/tv_pdv_product_special_price',
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

    #     "com.zalora.android:id/iv_bubble_bg"

        self.sizeDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/iv_bubble_bg",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }
        # "com.zalora.android:id/layout_add_to_bag"
        self.addToBagDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/layout_add_to_bag",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        self.cartDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/cart_button",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }


    def selectImageCampaign(self):

        self.mobileDriver.clickElement(self.imageCampaignDict)

    def selectFirstProduct(self):

        self.mobileDriver.clickElement(self.firstProductDict)

    def clickOnPrice(self):

        self.mobileDriver.clickElement(self.priceDict)

    def selectLSize(self):

        self.mobileDriver.clickElement(self.sizeDict,2)

    def addToBag(self):
        self.mobileDriver.clickElement(self.addToBagDict)

    def clickCartButton(self):
        self.mobileDriver.clickElement(self.cartDict)




