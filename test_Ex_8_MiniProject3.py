import pytest
import allure
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify that Trial is finished and current URL also")
@allure.description(
    "Verify the URL changes"
)
def test_mini_project_3():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    assert driver.current_url == "https://www.idrive360.com/enterprise/login"

    time.sleep(10)

    # Corrected the find_element method to match the selector
    Enter_username = driver.find_element(By.XPATH, "//input[@id='username' and @type='email']")
    Enter_username.send_keys("augtest_040823@idrive.com")

    time.sleep(10)

    Enter_password = driver.find_element(By.XPATH, "//input[@id='password' and @type='password']")
    Enter_password.send_keys("123456")

    time.sleep(10)

    checkbox = driver.find_element(By.XPATH, "//span[@class='id-checkmark']")
    checkbox.click()

    time.sleep(10)

    Click_Signin = driver.find_element(By.XPATH, "//button[@id='frm-btn' and @type='submit']")
    Click_Signin.click()

    time.sleep(10)
    # Verify that
    # Trial is finished and current URL

    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot')

    time.sleep(15)

    Click_upgrade_now = driver.find_element(By.XPATH, "//button[@class='id-btn id-warning-btn-drk id-tkn-btn' and "
                                                      "@style='display: block']")
    Click_upgrade_now.click()

    time.sleep(15)

    upgrade_now = driver.find_element(By.XPATH, "//h5[contains(@class,'id-card-title') and text()='Your free trial "
                                                "has expired']")
    assert upgrade_now.is_displayed()
    allure.attach(driver.get_screenshot_as_png(), name="upgrade_Screenshot")

    driver.close()
