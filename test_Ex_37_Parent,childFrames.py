import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def setup_driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_parent_child_siblings(setup_driver):
    driver = setup_driver
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    parent_frame_1 = driver.find_element(By.XPATH, "//frame[@name='frame-top']")

    driver.switch_to.frame(parent_frame_1)

    child_frame_1 = driver.find_element(By.XPATH, "//frame[@name='frame-left']")

    driver.switch_to.frame(child_frame_1)

    text1 = driver.find_element(By.XPATH, "//body").text

    print(text1)

    driver.switch_to.parent_frame()

    child_frame_2 = driver.find_element(By.XPATH, "//frame[@name='frame-middle']")

    driver.switch_to.frame(child_frame_2)

    text2 = driver.find_element(By.XPATH,"//body").text
    print(text2)

    driver.switch_to.parent_frame()

    child_frame_3 = driver.find_element(By.XPATH, "//frame[@name='frame-right']")

    driver.switch_to.frame(child_frame_3)

    text3 = driver.find_element(By.XPATH, "//body").text
    print(text3)

    driver.switch_to.default_content()

    parent_frame_2 = driver.find_element(By.XPATH, "//frame[@name='frame-bottom']")

    driver.switch_to.frame(parent_frame_2)

    text4 = driver.find_element(By.XPATH,"//body").text
    print(text4)






