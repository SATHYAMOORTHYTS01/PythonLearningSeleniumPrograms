from selenium import webdriver
from selenium.webdriver.common.by import By


# 1.Count no of rows and columns
# 2. read specific row & column data
# 3.
def test_028_WindowHandling():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://testautomationpractice.blogspot.com/")

    # 1.Count no of rows and columns
    noOfRows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
    noOfColoumns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
    print(noOfRows)  #7
    print(noOfColoumns)  #4

    # # 2. read specific row & column data

    data = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]")).text
    print(data)

    #3.Read all the rows adn columns

    # for r in range(2, noOfRows + 1):
    #     for c in range(1, noOfColoumns + 1):
    #         data = (driver.find_element(By.XPATH,
    #                                     "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]")).text
    #         print(data, end='       ')
    #
    #     print()

    #4. Read data based on the condition (List Books

    for r in range(2, noOfRows + 1):
        authorName = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]")).text
        if authorName == 'Animesh':
            bookName = (
                driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]")).text
            Subject = (
                driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[3]")).text
            price = (
                driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]")).text

            print(bookName, "     ", authorName,"     ",price,"      ",Subject)

