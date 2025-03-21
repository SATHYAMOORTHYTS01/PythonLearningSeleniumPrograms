import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


@pytest.mark.positive
@allure.title("Verify that url changes when we click on the Make appointment button ")
@allure.description(
    "Verify the URL changes"
)
def test_open_vwo_login():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    try:
        WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.NAME, 'username')))

        username_element = driver.find_element(By.NAME, 'username')
        username_element.send_keys("admin@admin.com")

        allure.attach(driver.get_screenshot_as_png(), name="username+login", attachment_type=AttachmentType.PNG)

        password_element = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-qa='jobodapuxe']")))
        password_element.send_keys("admin@123")

        allure.attach(driver.get_screenshot_as_png(), name="password+login", attachment_type=AttachmentType.PNG)

        sign_in_button = WebDriverWait(driver, timeout=10).until(
            EC.visibility_of_element_located((By.ID, "js-login-btn")))
        sign_in_button.click()

        allure.attach(driver.get_screenshot_as_png(), name="sign_in_button", attachment_type=AttachmentType.PNG)

    finally:
        driver.close()

