from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1400, 900)

driver.get("https://the-internet.herokuapp.com/checkboxes")

# Locate all checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# Verify the number of checkboxes
if len(checkboxes) == 2:
    print("PASS - Found 2 checkboxes.")
else:
    print(f"FAIL - Expected 2 checkboxes but found {len(checkboxes)}.")

# Display the properties of each checkbox
for i, checkbox in enumerate(checkboxes, start=1):
    print(f"\nCheckbox {i}")
    print(f"Displayed : {checkbox.is_displayed()}")
    print(f"Enabled   : {checkbox.is_enabled()}")
    print(f"Selected  : {checkbox.is_selected()}")

# Verify the default states
if not checkboxes[0].is_selected():
    print("\nPASS - Checkbox 1 is unchecked by default.")
else:
    print("\nFAIL - Checkbox 1 should be unchecked.")

if checkboxes[1].is_selected():
    print("PASS - Checkbox 2 is checked by default.")
else:
    print("FAIL - Checkbox 2 should be checked.")

# Click Checkbox 1
print("\nClicking Checkbox 1...")
checkboxes[0].click()

if checkboxes[0].is_selected():
    print("PASS - Checkbox 1 is now checked.")
else:
    print("FAIL - Checkbox 1 should be checked.")

# Click Checkbox 2 to uncheck it
print("\nClicking Checkbox 2...")
checkboxes[1].click()

if not checkboxes[1].is_selected():
    print("PASS - Checkbox 2 is now unchecked.")
else:
    print("FAIL - Checkbox 2 should be unchecked.")

input("\nPress Enter to close...")
driver.quit()