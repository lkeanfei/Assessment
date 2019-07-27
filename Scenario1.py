from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'Galaxy Tab A'
desired_caps['appPackage'] = 'com.zalora.android'
desired_caps['appActivity'] = 'pt.rocket.view.activities.SplashScreenActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@resource-id='com.zalora.android:id/title' and @text='SELECT LOCATION']")))

malaysiaSelection = driver.find_element_by_xpath("//*[@resource-id='com.zalora.android:id/splash_item_name' and @text='MALAYSIA']")
malaysiaSelection.click()


wait.until(EC.element_to_be_clickable((By.ID, 'com.zalora.android:id/splash_item_name')))

englishSelection = driver.find_element_by_xpath("//*[@resource-id='com.zalora.android:id/splash_item_name' and @text='ENGLISH']")
englishSelection.click()

# Wait
# # 	com.zalora.android:id/facebook_login
# loginFacebookBtn = driver.find_element_by_xpath("//*[@resource-id='com.zalora.android:id/facebook_login']")
# loginFacebookBtn.click()

wait.until(EC.element_to_be_clickable((By.ID, 'com.zalora.android:id/skip_button')))
skipButton = driver.find_element_by_id('com.zalora.android:id/skip_button')
skipButton.click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@resource-id='com.zalora.android:id/segment']")))
shopMenBtn = driver.find_element_by_xpath("//*[@resource-id='com.zalora.android:id/segment' and @text='SHOP MEN']")
shopMenBtn.click()

wait.until(EC.element_to_be_clickable((By.ID, "com.zalora.android:id/tutorial_skip_button")))
skipTutorialButton = driver.find_element_by_id('com.zalora.android:id/tutorial_skip_button')
skipTutorialButton.click()


# 	Navigate up

wait.until(EC.element_to_be_clickable((By.ID,"com.zalora.android:id/img_campaign")))
campaignBanner = driver.find_element_by_id('com.zalora.android:id/img_campaign')
campaignBanner.click()

# Select the first item
wait.until(EC.element_to_be_clickable((By.ID,"com.zalora.android:id/image_view")))
firstProduct = driver.find_element_by_id('com.zalora.android:id/image_view')
firstProduct.click()

#Click on the price
wait.until(EC.element_to_be_clickable((By.ID,"com.zalora.android:id/tv_pdv_product_special_price")))
priceElement = driver.find_element_by_id('com.zalora.android:id/tv_pdv_product_special_price')
priceElement.click()

# 	com.zalora.android:id/iv_bubble_bg
wait.until(EC.element_to_be_clickable((By.ID,"com.zalora.android:id/iv_bubble_bg")))
sizeElements = driver.find_elements_by_id('com.zalora.android:id/iv_bubble_bg')
sizeElements[2].click()

addToBag = driver.find_element_by_id("com.zalora.android:id/layout_add_to_bag")
addToBag.click()

cartButton = driver.find_element_by_id("com.zalora.android:id/cart_button")
cartButton.click()


wait.until(EC.element_to_be_clickable((By.ID, "com.zalora.android:id/button_image")))
searchButtonImages = driver.find_elements_by_id('com.zalora.android:id/button_image')
searchButtonImages[0].click()


wait.until(EC.element_to_be_clickable((By.ID, "com.zalora.android:id/search_field")))
searchField = driver.find_element_by_id('com.zalora.android:id/search_field')
searchField.send_keys("Polo shirt" + Keys.ENTER)
searchField.send_keys(Keys.ENTER)

print("")

# shop MEN
# com.zalora.android:id/segment , 	SHOP MEN

# com.zalora.android: id / tutorial_skip_button

# Skip tutorial button

windowSize = driver.get_window_size()
width = windowSize['width']
height = windowSize['height']

startX = 0.9 *width
startY = 0.5*height
endX = 0.1* width
endY = 0.5*height

driver.swipe(start_x= startX , start_y= startY , end_x=endX , end_y= endY)
driver.swipe(start_x= startX , start_y= startY , end_x=endX , end_y= endY)


okBtn = driver.find_element_by_id('com.shopee.my:id/ok')
okBtn.click()

startBtn = driver.find_element_by_id('com.shopee.my:id/btn')