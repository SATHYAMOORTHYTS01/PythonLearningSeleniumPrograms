import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_027_Frames():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("http://demo.automationtesting.in/Frames.html")

    driver.find_element(By.XPATH, "//a[text()='Iframe with in an Iframe']")

    time.sleep(5)
    outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
    driver.switch_to.frame(outerframe)
    time.sleep(5)

    innerframe = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")
    driver.switch_to.frame(innerframe)

    time.sleep(5)
    input_box = driver.find_element(By.XPATH, "//input[@type='text']")
    input_box.send_keys("Welcome")
    driver.switch_to.parent_frame()

    driver.quit()