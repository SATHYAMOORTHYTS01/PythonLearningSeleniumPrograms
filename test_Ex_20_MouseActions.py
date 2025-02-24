import time

from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.by import By


def test_019_actions():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #click = normaldriver , will ind the element and click on i t, release it
    # click and hold -

    atag = driver.find_element(By.ID, "click")
    atag.click()

    time.sleep(5)
    #Actions Builders - Mouse interations

    actions_builders = ActionBuilder(driver)
    actions_builders.pointer_action.pointer_up(MouseButton.BACK)
    actions_builders.perform()
