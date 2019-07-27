from lib.MobileDriver import MobileDriver
from lib.MobileDriver import MOBILEFINDTAGS
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self , mobileDriver: MobileDriver):

        self.mobileDriver = mobileDriver

        self.loginPageDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG : By.ID,
            MOBILEFINDTAGS.ANDROIDTAG : "com.zalora.android:id/facebook_login",
            MOBILEFINDTAGS.IOSBYTAG : "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",

        }

        self.loginToFacebookDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/facebook_login",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        self.facebookLoginFormDict = {
            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "login_form",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        self.userNameDict = {

        MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
        MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/edit_text",
        MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
        MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        self.passwordDict = {

            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/password_field_id",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

        self.loginButtonDict = {

            MOBILEFINDTAGS.ANDROIDBYTAG: By.ID,
            MOBILEFINDTAGS.ANDROIDTAG: "com.zalora.android:id/login_button",
            MOBILEFINDTAGS.IOSBYTAG: "Not implmented",
            MOBILEFINDTAGS.IOSTAG: "Not implmented",
        }

    def exists(self):



        return self.mobileDriver.elementExists(self.loginPageDict)

    def clickLoginToFacebook(self):

        return self.mobileDriver.clickElement(self.loginToFacebookDict)


    def facebookLoginFormExists(self):

        contextList = self.mobileDriver.getAllContexts()

        assert "WEBVIEW" in contextList  , "WEBVIEW context is not available. Available contexts are " + ",".join(contextList)

        return self.mobileDriver.elementExists(self.facebookLoginFormDict)

    def enterUserName(self):

        self.mobileDriver.enterText(self.userNameDict , "digixcheckout@gmail.com")


    def enterPassword(self):

        self.mobileDriver.enterText(self.passwordDict , "digix123!@")

    def clickLoginButton(self):

        self.mobileDriver.clickElement(self.loginButtonDict)

