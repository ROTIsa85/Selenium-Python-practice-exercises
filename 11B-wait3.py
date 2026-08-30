#Exercise 11B3 — !!!! Explicit Wait: visibility_of_element_located
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

wait = WebDriverWait(driver, 10)

# Step 1 - Locate the Remove button and click it
remove_button = driver.find_element(By.XPATH, "//button[text()='Remove']")
remove_button.click()

# Step 2 - Wait until the checkbox is no longer present
wait.until(
    EC.invisibility_of_element_located(
        (By.ID, "checkbox")
    )
)

print("Checkbox removed")

# Step 3 - Locate the Add button and click it
add_button = driver.find_element(By.XPATH, "//button[text()='Add']")
add_button.click()

# Step 4 - Wait until the checkbox is visible
checkbox = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "checkbox")
    )
)

# Step 5 - Verify the checkbox is displayed
assert checkbox.is_displayed()

print("Checkbox is visible")

driver.quit()

