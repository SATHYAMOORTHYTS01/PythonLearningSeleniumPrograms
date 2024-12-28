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

    driver.implicitly_wait(20)

    username_element = driver.find_element(By.NAME, "username")
    username_element.send_keys("admin@admin.com")

    password_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    password_element.send_keys("admin@123")

    # Click Sign In button
    sign_in_button = driver.find_element(By.ID, "js-login-btn")
    sign_in_button.click()
