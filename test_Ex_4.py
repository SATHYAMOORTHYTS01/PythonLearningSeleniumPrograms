from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options
import time

def test_open_vwologin():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/#/login.com")
    print(driver.page_source)
    driver.close()
