import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_022_actions():
    # Initialize WebDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://omayo.blogspot.com/")
    links = driver.find_elements(By.XPATH, "//div[@id='LinkList1']//a")

    for link in links:

        actions = ActionChains(driver)
        actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        time.sleep(3)

    driver.quit()
