import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Handling SVG by searching Tripura State")
@allure.description(
    "Handling SVG - find and click Tripura State"
)
def test_flipkart_search_AC():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    time.sleep(5)

    states = driver.find_elements(By.XPATH, "//*[name()='svg']"
                                            "/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name("
                                            ")='path']")

    for state in states:

        print(state.get_attribute("aria-label"))

        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="Tripura_Clicked", attachment_type=AttachmentType.PNG)
