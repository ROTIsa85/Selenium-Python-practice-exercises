from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.set_window_size(1400, 900)
driver.get("https://the-internet.herokuapp.com/checkboxes")

one_checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
print("HTML:", one_checkbox.get_attribute("outerHTML"))

checkboxes = driver.find_elements(
    By.CSS_SELECTOR,"input[type='checkbox']")

print(f"there are {len(checkboxes)} checkboxes")

for i, checkbox in enumerate(checkboxes, start=1):
    print(f"\ncheckbox {i} is displayed, {checkbox.is_displayed()}")
    print(f"\ncheckbox {i} is enabled, {checkbox.is_enabled()}")
    print(f"\ncheckbox {i} is selected, {checkbox.is_selected()}")

checkboxes[0].click()
for i, checkbox in enumerate(checkboxes, start=1):
    if checkbox.is_selected():
        print(f"PASS - Checkbox {i} is selected")
    else:
        print(f"FAIL - Checkbox {i} is not selected")
checkboxes[1].click() # click 2nd checkbox
if not checkboxes[1].is_selected():
    print("PASS - after click, checkbox 2 is now unselected.")
else:
    print("FAIL - Checkbox 2 is still selected.")


input("Enter to quit")
driver.quit()