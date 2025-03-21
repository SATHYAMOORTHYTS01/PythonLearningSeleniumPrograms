from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# 1.Count no of rows and columns
# 2. read specific row & column data
def test_031_DynamicWebtable():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(
        "Admin")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(
        "admin123")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

    # Admin
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Admin']"))).click()

    # User Management

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='User Management ']"))).click()

    # Users
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
        By.XPATH, "//a[@role='menuitem']"))).click()

    # Wait for the table to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='table']")))

    # Get all rows
    rows = driver.find_elements(By.XPATH, "//div[@role='row']")
    print(f"Total rows found: {len(rows) - 1}")  # Subtract 1 to ignore the header row

    # Loop through each row and check if the role is 'ESS'
    for row in rows[1:]:  # Skipping the header row
        try:
            username = row.find_element(By.XPATH, ".//div[@role='cell'][1]").text
            role = row.find_element(By.XPATH, ".//div[@role='cell'][3]").text  # Assuming role is in 3rd column

            if role.strip() == "ESS":
                print(f"Username: {username}, Role: {role}")
        except Exception as e:
            print(f"Skipping row due to error: {e}")

    driver.quit()
