import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify that  url changes")
@allure.description(
    "Verify the URL changes"
)
def test_mini_project_4():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"

    time.sleep(20)

    click_make_appoinment = driver.find_element(By.XPATH,
                                                "//a[@id='btn-make-appointment' and text()='Make Appointment']")
    click_make_appoinment.click()

    # verify the Url changes

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)

    Enter_username = driver.find_element(By.XPATH, "//input[@id='txt-username' and @name='username']")
    Enter_username.send_keys("John Doe")

    Enter_password = driver.find_element(By.XPATH, "//input[@id='txt-password' and @name='password']")
    Enter_password.send_keys("ThisIsNotAPassword")

    Click_login = driver.find_element(By.XPATH, "//button[@id='btn-login' and text()='Login']")
    Click_login.click()

    allure.attach(driver.get_screenshot_as_png(), name="appointment-screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    driver.quit()
