import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_026_AlertsAuthenticated():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    JS_Alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")

    JS_Alert.click()

    JS_Alert = driver.switch_to.alert
    print(JS_Alert.text)

    JS_Alert.accept()

    verify = driver.find_element(By.ID, "result").text

    print("Result",verify)






