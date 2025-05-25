import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


def test_022_windows():
    # Initialize WebDriver
    driver: WebDriver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.spicejet.com/")

    source = driver.find_element(By.XPATH, "//div[@data-testid='to-testID-origin']")

    actions = ActionChains(driver)
    actions.move_to_element(source).click().perform()
    actions.send_keys_to_element(source, "BLR").perform()

    time.sleep(5)

    driver.quit()
