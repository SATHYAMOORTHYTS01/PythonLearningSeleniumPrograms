import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_019_actions():
    # Initialize WebDriver
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")


    close_modal = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-cy='closeModal']"))
    )
    close_modal.click()

    from_date = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "fromCity"))
    )

    actions = ActionChains(driver)

    actions.move_to_element(from_date).click().send_keys("Mumbai").send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.ENTER).perform()

    driver.quit()
