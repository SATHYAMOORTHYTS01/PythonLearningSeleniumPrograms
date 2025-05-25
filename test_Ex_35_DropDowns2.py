from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_035_Dropdowns2():
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")

    wait = WebDriverWait(driver, 10)

    # Find all iframes
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Total iframes found: {len(iframes)}")

    # Try switching to each iframe and check for dropdown
    for index, iframe in enumerate(iframes):
        driver.switch_to.default_content()  # Reset frame context
        driver.switch_to.frame(iframe)

        try:
            dropdown = wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
            print(f"Dropdown found in iframe index {index}")
            break  # Stop looping once found

        except:
            print(f"No dropdown in iframe index {index}")
            continue

    # Select "India"
    dropdown = wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
    select = Select(dropdown)
    select.select_by_visible_text("India")

    # Verify selection
    selected_option = select.first_selected_option.text
    assert selected_option == "India", f"Expected 'India', but got '{selected_option}'"
    print(f"Successfully selected: {selected_option}")

    driver.quit()
