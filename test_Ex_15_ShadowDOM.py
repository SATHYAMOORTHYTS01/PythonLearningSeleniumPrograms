import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.mark.positive
@allure.title("Shadow DOM")
@allure.description(
    "Input the value in pizza name"
)
def test_flipkart_search_AC():
    driver = webdriver.Edge()
    driver.maximize_window()

    # Open the URL
    driver.get('https://selectorshub.com/xpath-practice-page/')

    username = driver.execute_script("""
        return document
            .querySelector('div.jackPart')
            .shadowRoot.querySelector('input#kils')""")

    username.send_keys("Sathya")

    # Use JavaScript to locate the element in the Shadow DOM
    pizza = driver.execute_script("""
        return document.querySelector('div.jackPart')
            .shadowRoot.querySelector('div#app2')
            .shadowRoot.querySelector('input#pizza');
    """)

    # Send keys to the input field
    pizza.send_keys("FarmHouse")

    allure.attach(driver.get_screenshot_as_png(), name="Username,Pizza", attachment_type=AttachmentType.PNG)

    # Wait to observe the result
    time.sleep(10)

    # Close the browser
    driver.quit()
