import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_026_AlertsAuthenticated():
    driver = webdriver.Edge()
    driver.maximize_window()

    # driver.get("https://the-internet.herokuapp.com/digest_auth")

    #inject username and passwrod in the URL and bypass it
    driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
