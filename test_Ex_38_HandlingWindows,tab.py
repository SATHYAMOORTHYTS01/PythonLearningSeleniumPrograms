from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def setup_driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.refresh()
    yield driver
    driver.quit()


def test_038_windows_tab(setup_driver):
    driver = setup_driver
    driver.get("https://omayo.blogspot.com/")
    wait = WebDriverWait(driver, 10)

    main_window = driver.current_window_handle


    # Open all links under "Other Sites to Practice"
    links = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@id='LinkList1']//a")))

    for link in links:
        ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
        time.sleep(1)

    time.sleep(3)  # Wait for all tabs to open

    all_windows = driver.window_handles

    # Print all window titles and close other than 3rd and main
    for window_handle in driver.window_handles:
        if window_handle != main_window:
            driver.switch_to.window(window_handle)
            driver.close()

    # Switch to the 3rd window if it exists
    if len(driver.window_handles) >= 3:
        third_window = driver.window_handles[2]
        driver.switch_to.window(third_window)
        print("Switched to 3rd window:", driver.title)

        try:
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Themes"))).click()
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//label[text()='Standard']//span[@class='ui-checkboxradio-icon-space']"))).click()
        except Exception as e:
            print("Element not found or click failed:", e)

        driver.close()
    #
    # # Switch back to the main window
    # driver.switch_to.window(main_window)
    # print("Back to Main Window:", driver.title)
    #
    # # Open new tab and navigate to Selenium blog
    # driver.switch_to.new_window('tab')
    # driver.get("https://selenium143.blogspot.com/")
    # driver.find_element(By.LINK_TEXT, "What is Selenium?").click()
    # print("Page Title (Selenium blog):", driver.title)
    #
    # driver.quit()

