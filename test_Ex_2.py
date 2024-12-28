from selenium import webdriver
import time


def test_open_vwologin():
    driver = webdriver.Chrome()  # Initialize Chrome WebDriver

    # Here you would typically perform an HTTP POST request, but it's commented out for now.
    # Example: Make the POST request here (using requests library, etc.)

    # Print the session ID

    print(driver.session_id)  #6cf4f01aebd392ca09dc70075790411a
    driver.get("https://app.vwo.com")
    print(driver.title)
    time.sleep(10)  # Keep the browser open for 10 seconds
    assert driver.title == "Login - VWO"  # his line checks if the page title is equal to "Login - VWO". If this
    # condition is not met
    driver.quit()  # Close the browser session
