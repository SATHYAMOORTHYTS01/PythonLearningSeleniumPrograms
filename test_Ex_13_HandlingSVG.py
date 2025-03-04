import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Handling Search button SVG")
@allure.description(
    "Handling SVG"
)
def test_flipkart_search_AC():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")

    search_input = driver.find_element(By.XPATH, "//input[@type='text']")
    search_input.send_keys("AC")

    svg_list = driver.find_element(By.XPATH, "//*[local-name()='svg']")
    actions = ActionChains(driver)
    actions.move_to_element(svg_list).click().perform()







