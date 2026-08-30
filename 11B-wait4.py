#Exercise 11B4 — Explicit Wait: element_to_be_clickable
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

wait = WebDriverWait(driver, 10)

# Step 1 - Wait until the Remove button is clickable
remove_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[text()='Remove']")
    )
)

# Step 2 - Click the Remove button
remove_button.click()

# Step 3 - Wait until the checkbox disappears
wait.until(
    EC.invisibility_of_element_located(
        (By.ID, "checkbox")
    )
)

# Step 4 - Verify the checkbox is no longer visible
print("Checkbox removed successfully")

driver.quit()