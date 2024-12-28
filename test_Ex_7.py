import pytest
import allure
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify that url changes when we click on the Make appointment button ")
@allure.description(
    "Verify the URL changes"
)
def test_open_vwologin():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    # id --> name --> class_name --> link/partial link)anchor tag) --> css selector --> xpath

    # Enter username
    username_element = driver.find_element(By.NAME, "username")
    username_element.send_keys("admin@admin.com")

    # Elements
    # < input
    # type = "password"
    # class ="text-input W(100%)"
    # name="password"
    # id="login-password" d
    # ata-qa="jobodapuxe"
    # Enter password

    password_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_element.send_keys("admin@123")

    # Click Remember Me checkbox
    checkbox_remember_me = driver.find_element(By.CSS_SELECTOR, "use[href*='checkbox-button']")
    checkbox_remember_me.click()

    # Click Sign In button
    sign_in_button = driver.find_element(By.ID, "js-login-btn")
    sign_in_button.click()

    time.sleep(10)
