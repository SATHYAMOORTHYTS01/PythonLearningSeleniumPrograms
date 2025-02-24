import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_022_windows():
    # Initialize WebDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")

    parent_window = driver.current_window_handle #1 window
    print(parent_window)

    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    window_handles = driver.window_handles #2 window
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle) #child
        if "New Window" in driver.page_source:
            print("Testcase Passes!!")
            break

    time.sleep(5)

    driver.quit()