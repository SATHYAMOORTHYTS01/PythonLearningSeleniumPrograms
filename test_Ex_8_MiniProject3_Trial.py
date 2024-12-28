"""
Open the URL - https://www.idrive360.com/enterprise/login
Enter the username, password
Verify that Trial is fnished and current URL also
Add a logic to add Allure Screen for the Trial end """

# augtest_040823@idrive.com
# 123456


import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify the Upgrade Now button ")
@allure.description("Verify that Trial is finished message is coming and current URL also updated")
def test_mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")

    username_web_element = driver.find_element(By.ID, "username")
    username_web_element.send_keys("augtest_040823@idrive.com")

    password_web_element = driver.find_element(By.ID, "password")
    password_web_element.send_keys("123456")

    signin_web_element = driver.find_element(By.ID, "frm-btn")
    signin_web_element.click()

    time.sleep(10)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true"
    time.sleep(5)
    driver.quit()
