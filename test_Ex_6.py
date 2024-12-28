import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # Import Options
import time
from selenium.webdriver.common.by import By

@pytest.mark.positive
@allure.title("Verify that url changes when we click on the Make appointment button ")
@allure.description(

    "Verify the URL changes"
)
def test_open_katalon():
    webdriver.Edge()
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options)
    driver.back()
    driver.refresh()
    driver.forward()
    chrome_options.add_argument("--page-load-strategy=none")
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # find the element
    # we need to find the unique attribute
    # approach of finding element
    # first go with id => ame - > classname -> link -> ccss selctor -> x path
    # <input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi" >

    make_appointment_element = driver.find_element("id", "btn-make-appointment")
    # click on it
    make_appointment_element.click()
    # verify the link
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(10)
    driver.quit()

