from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_028_WindowHandling():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://ui.vision/demo/webtest/frames/")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/span[text()='Next']")))
