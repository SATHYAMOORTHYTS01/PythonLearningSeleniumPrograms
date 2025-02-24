import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_019_actions():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    # first_name.send_keys("sathya")

    time.sleep(10)
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(
        first_name, "thetestingacademy").key_up(
        Keys.SHIFT).context_click().perform()
