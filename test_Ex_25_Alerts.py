import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_025_Alerts():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()'] ").click()

    time.sleep(5)

    alertwindow = driver.switch_to.alert

    print(alertwindow.text)

    alertwindow.send_keys("Welcome Sathya")

    # alertwindow.accept() #close alert window by using OK button

    alertwindow.dismiss()  #close alert window by using Cancel button
