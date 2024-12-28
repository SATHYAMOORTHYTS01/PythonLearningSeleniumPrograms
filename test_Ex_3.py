from selenium import webdriver
from selenium.webdriver.chrome import session_id
from selenium.webdriver.chrome.options import Options  # Import Options
import time

def test_open_vwologin():
    # Options class - used to customize the behavior of the ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Start the browser in incognito mode
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options)  # Initialize Chrome WebDriver with options
    driver.get("https://app.vwo.com/#/login")  # Navigate to the specified URL
    print(driver.title)  # Print the title of the page
    print(session_id())
    assert driver.title == "Login - VWO"  # Assert that the title matches the expected value
    time.sleep(10)  # Keep the browser open for 10 seconds
    driver.quit()  # It's a good practice to close the browser after the test

