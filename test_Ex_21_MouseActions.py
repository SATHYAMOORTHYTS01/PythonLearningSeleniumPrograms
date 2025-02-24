import time

from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


def test_019_actions():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #click = normaldriver , will ind the element and click on i t, release it
    # click and hold -

    element_to_hold = driver.find_element(By.ID, "draggable")


    time.sleep(5)
    #Actions Builders - Mouse interations

    actions_builders = ActionBuilder(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()


