from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_034_Dropdowns():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Photo%20Manager")

    # driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'iframe.demo-frame'))
    #
    # actions = ActionChains(driver)
    # image_1 = driver.find_element(By.XPATH, "//h5[@class='ui-widget-header' and text()='High Tatras']")
    # trash = driver.find_element(By.ID, 'trash')
    #
    # actions.drag_and_drop(image_1, trash).perform()


