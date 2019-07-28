# Assessment

The tests are written in Python and they are developed based on Pytest framework.
Make sure that you have Python 3.7 installed on your system and execute 

```python
pip install -r requirements.txt
```

As there is no app selected for the tests , I have used the Zalora app available from Google Playstore. Since it is the official release of the app ,
there are some limitations for Appium auto tests.


##  Running the tests

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
