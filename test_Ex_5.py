from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options
import time

def test_open_vwologin():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login.com")
    print(driver.page_source)
    driver.refresh()
    driver.back()
    driver.forward()
    time.sleep(10)
    driver.quit()


    # quit - will close all teh tab's
    # close - closes the current tab alone


