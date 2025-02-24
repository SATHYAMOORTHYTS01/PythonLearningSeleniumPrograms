from telnetlib import EC

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
@pytest.mark.positive
@allure.title("Verify the invalid login with the excel Testdata")
@allure.description(
    "TC#1 invalid login check on vwo.login.com"
)
class TestAlerts:

    def TC1_JSAlerts(self):

        self.driver = webdriver.Edge()
        options = webdriver.EdgeOptions()
        options.page_load_strategy = "normal"
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        elements = self.driver.find_element(By.XPATH, "https://the-internet.herokuapp.com/javascript_alerts")
        elements.click()

        WebDriverWait(driver=self.driver, timeout=10).until(EC.alert_is_present())

        alert = Alert(self.driver)
        print()


        assert result == "You successfully clicked an alert"




