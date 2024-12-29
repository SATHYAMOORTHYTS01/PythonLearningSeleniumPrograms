import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select

@pytest.mark.positive
@allure.title("Verify that  url changes")
@allure.description(
    "Verify the URL changes"
)
def test_vwo_login_select():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    element_dropdown = driver.find_element(By.ID, "dropdown")

    select = Select(element_dropdown)

    select.select_by_index("0")


    # Types of dropdowns
    # 1. Static - select class is used
    # 2. Dynamic - one can be static with custom controls - they can be only executed by js executor
    #              pure dynamic - JS,ACTIONS,LOGIC



