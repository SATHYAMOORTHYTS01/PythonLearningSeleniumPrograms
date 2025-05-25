import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def test_036_keyboardaction():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://omayo.blogspot.com/")

    wait = WebDriverWait(driver, 10)

    text_area = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "widget-content")))

    act = ActionChains(driver)

    time.sleep(4)

    act.move_to_element(text_area).click().perform()
    act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    test_box = driver.find_element(By.ID, "ta1")

    time.sleep(4)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    act.send_keys(Keys.TAB)
    time.sleep(4)
    act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


