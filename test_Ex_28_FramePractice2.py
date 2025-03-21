import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_027_Frames():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://ui.vision/demo/webtest/frames/")

    # Frame 1
    driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@src='frame_1.html']"))

    Frame1_Input = WebDriverWait(driver, timeout=10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='mytext1']")))

    Frame1_Input.send_keys("Hello")

    driver.switch_to.default_content()

    # Frame 2

    driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@src='frame_2.html']"))

    Frame2_Input = WebDriverWait(driver, timeout=10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='mytext2']")))
    Frame2_Input.send_keys("Hey Buddy")

    driver.switch_to.default_content()

    # Frame 3

    driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@src='frame_3.html']"))

    Frame3_Input = WebDriverWait(driver, timeout=10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@name='mytext3']")))
    Frame3_Input.send_keys("Hey NAVIGATE TO iFRAME")

    # INNER FRAME
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='teQAzf']"))
    )

    Question1 = driver.find_element(By.XPATH, "//div[@class='AB7Lab Id5V1']")
    Question1.click()

    Question2 = driver.find_element(By.XPATH, "(//div[@class='uHMk6b fsHoPb'])[1]")
    Question2.click()

    time.sleep(5)
    Question2 = driver.find_element(By.XPATH, "(//div[@class='uHMk6b fsHoPb'])[2]")
    Question2.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'MocG8c')]"))
    )

    # Get all options
    options = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@role='option']"))
    )

    index_to_select = 1

    for i, option in enumerate(options):
        if i == index_to_select:
            ActionChains(driver).move_to_element(option).click().perform()
            break

    # Wait for dropdown option
    option_to_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='MocG8c HZ3kWc mhLiyf OIC90c LMgvRb' and @jsname='wQNmvb' "
                                              "and @data-value='Well, now I know :-)' and @tabindex='-1']"))
    )
    option_to_select.click()

    # WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.XPATH, "//div[@class='MocG8c HZ3kWc mhLiyf
    # OIC90c LMgvRb' and @jsname='wQNmvb' " "and @data-value='Well, now I know :-)' and @tabindex='-1']")) ).click()

    time.sleep(1)

    # Click 'Next' button
    Click_Next = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
    )
    Click_Next.click()

    driver.quit()
