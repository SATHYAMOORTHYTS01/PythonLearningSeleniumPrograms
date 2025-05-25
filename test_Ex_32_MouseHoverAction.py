import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# 1.Count no of rows and columns
# 2. read specific row & column data
def test_032_MouseHoverAction():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://testautomationpractice.blogspot.com/")

    act = ActionChains(driver)

    #MouseHover
    PointMe = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
    act.move_to_element(PointMe).click().perform()

    driver.find_element(By.XPATH, "//a[text()='Laptops']").click()

    feild1 = driver.find_element(By.XPATH, "//input[@id='field1']")
    feild1.clear()

    feild1.send_keys("WelcomeSathya")

    #DoubleClickAction
    Copy_text_ele = driver.find_element(By.XPATH, "//button[@ondblclick='myFunction1()']")
    act.double_click(Copy_text_ele).perform()

    #Drag and Drop
    target1 = driver.find_element(By.XPATH, "//div[@id='draggable']")
    target2 = driver.find_element(By.XPATH, "//div[@id='droppable']")

    act.drag_and_drop(target1, target2).perform()
    time.sleep(5)

    driver.quit()
