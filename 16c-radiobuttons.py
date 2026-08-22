#this version of the script checks status of radio buttons 1 and 2 after click of radio button 2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.set_window_size(1400, 900)

driver.get("https://demoqa.com/radio-button")

# Find all radio buttons
radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print("Number of radio buttons:", len(radio_buttons))
# Find labels associated with the radio buttons.
# The radio input itself may not be directly visible.
labels = driver.find_elements(
    By.CSS_SELECTOR,
    "label.form-check-label")
#HTML of all labels:
for i, label in enumerate(labels, start=1):
    print(f"\nLabel {i}")
    print("HTML      :", label.get_attribute("outerHTML"))
    print("Text      :", label.text)
    print("FOR: ", label.get_attribute("for"))
print() 
for i, radio in enumerate(radio_buttons, start=1):
    print(f"\nRadio {i}")
    print(f"HTML      : {radio.get_attribute('outerHTML')}")
    print(f"Value     : {radio.get_attribute('value')}")
    print(f"Displayed : {radio.is_displayed()}")
    print(f"Enabled   : {radio.is_enabled()}")
    print(f"Selected  : {radio.is_selected()}")
    print(f"ID        : {radio.get_attribute('id')}")
####################### 

# Print initial Selected state
print() 
print("Before click radio buttons Selected state:")
for i, radio in enumerate(radio_buttons, start=1):
    if radio.is_selected():
        print("Selected")
    else:
        print("Not selected")       
if len(labels) >= 2:
    print(f"PASS - Expected at least 2 labels, found {len(labels)}")
    labels[1].click()
else:
    print(f"FAIL - Expected at least 2 labels, found {len(labels)}")

print()  
if (not radio_buttons[0].is_selected()) and radio_buttons[1].is_selected():
    print("PASS - Radio button group behaves correctly.")
else:
    print("FAIL - Radio button group behaves incorrectly.")     
#use also assert to practice
assert (
    (not radio_buttons[0].is_selected())
    and radio_buttons[1].is_selected()
), "FAIL - Radio button behaviour is incorrect." 
  
time.sleep(10) 

driver.quit()
