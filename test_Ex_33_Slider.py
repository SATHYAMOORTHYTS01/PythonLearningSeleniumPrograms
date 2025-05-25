import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_033_Slider():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://testautomationpractice.blogspot.com/")

    act = ActionChains(driver)
    wait = WebDriverWait(driver, 10)

    # Wait until slider handles are visible & clickable
    POINTER1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all "
                                                                "ui-state-default'])[1]")))
    POINTER2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all "
                                                                "ui-state-default'])[2]")))

    # Scroll into view (in case it's not visible)
    driver.execute_script("arguments[0].scrollIntoView();", POINTER1)
    driver.execute_script("arguments[0].scrollIntoView();", POINTER2)

    print("Location of Slider Before Moving......")
    print("POINTER1:", POINTER1.location)
    print("POINTER2:", POINTER2.location)

    # Move the first slider handle (start handle) slightly right
    act.click_and_hold(POINTER1).move_by_offset(30, 0).release().perform()
    time.sleep(2)

    # Move the second slider handle (end handle) further right
    act.click_and_hold(POINTER2).move_by_offset(60, 0).release().perform()
    time.sleep(2)

    # Re-fetch slider positions
    POINTER1 = driver.find_element(By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
    POINTER2 = driver.find_element(By.XPATH, "(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")

    print("Location of Slider After Moving......")
    print("POINTER1:", POINTER1.location)
    print("POINTER2:", POINTER2.location)

    driver.quit()
