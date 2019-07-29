# Assessment

The answers for Section 1 is documented inside the file Digix Lightning Assessment Answers.docx

For section 2 ,the tests are written in Python and they are developed based on Pytest framework.
Make sure that you have Python 3.7 installed on your system and execute 

```python
pip install -r requirements.txt
```

As there is no app selected for the tests , I have used the Zalora app available from Google Playstore. Since it is the official release of the app ,
there are some limitations for Appium auto tests.

## Setup the tests
- Install the Zalora App from Google playstore , https://play.google.com/store/apps/details?id=com.zalora.android&hl=en
- Download and install Node.js (LTS version) from https://nodejs.org/en/download/
- Download and install Android Studio and Android SDK
- Setup the environment variable ANDROID_HOME to 
```
C:\Users\<YourUser>\AppData\Local\Android\Sdk
```

- Start a command prompt and install appium
```
npm install -g appium@1.13.0
```
- Start a command prompt and execute the following command to start the Appium Server
```
appium
```


##  Running the tests
There are 2 automated tests , test_scenario1.py and test_scenario2.py. Both are BDD tests which have their respective
Gherkin files defined in their feature files.

The tests are designed in a way to maximize reusability. Page Object libraries are created to encapsulate the page properties and actions.

The same tests can be run on both Android and iOS without much modification , as the differences in the XPath are encapsulated in the page object libraries.

The tests can be run on Android by executing

```
pytest --os=Android
```

or for running on iOS (currently not supported , due to the limitations mentioned below)


```
pytest --os=iOS
```

## Test results

The test results are output as Junit files and here is a sample of the test results 

```
<testsuite disabled="0" errors="0" failures="0" name="test_scenario2.py" skipped="0" tests="1" time="32.09598731994629">
<testcase name="test_Scenario2_OrderTransaction" time="32.095987">
<system-out>
Given that Country and Language Selection has completed....passed
When I select and add product to cart....passed
Then I should be able to checkout successfully....passed
</system-out>
		</testcase>
	</testsuite>
```
# Limitations

1. WebView is not available 
>For Scenario 1 - Facebook Login to be fully automated , Appium needs to be able to detect the WebView in App. 

>The developer will need to setWebContentsDebuggingEnabled in the app for Facebook login to proceed ,since the Facebook Login form is HTML based.

>Kindly refer to the link 
>https://developer.android.com/reference/android/webkit/WebView.html#setWebContentsDebuggingEnabled(boolean)

2. iOS Code-Signing problem
>The Zalora app is code-signed and prohibits unidentified developer do the coding and try to run the app on various devices.

>In this case , there will be problems identifying the elements on the App for iOS devices.

>Hence ,iOS automation is currently not supported.
>Refer to the following links for futher information
> https://stackoverflow.com/questions/51160718/run-appium-automation-without-code-signing 
> https://stackoverflow.com/questions/32728649/how-to-test-any-ios-app-with-appium


3. Paypal sandbox test account 
> For the tests to be able to complete the Paypal payment , it would require the app developer to enable sandbox test account on their account


# Debugging tips

- If you are seeing the following error during the test run 

```
 selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: Could not proxy command to remote server. Original error: Error: socket hang up
..\digixvenv\lib\site-packages\selenium\webdriver\remote\errorhandler.py:242: WebDriverException
```