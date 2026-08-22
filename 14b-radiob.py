from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.set_window_size(1400, 900)

wait = WebDriverWait(driver, 10)
driver.get(
    "https://demoqa.com/radio-button"
)

# Find all radio buttons
radio_buttons = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print("Number of radio buttons:", len(radio_buttons))

for i, radio in enumerate(radio_buttons, start=1):
    print(f"Radio {i}:")
    print("  selected:", radio.is_selected())
    print("  enabled :", radio.is_enabled())
    print("  displayed:", radio.is_displayed())
    print("  value:", radio.get_attribute("value"))
    print()
    
# Print initial state
print("before click: button is selected or not:")
for i, radio in enumerate(radio_buttons, start=1):
    print(f"Radio {i}: {radio.is_selected()}")
#by attribute = id 
print()
print("radio buttons by the id:")
for radio in radio_buttons:
    print(
        f"{radio.get_attribute('id')}: "
        f"{radio.is_selected()}"
    )
#click first found enabled radio button:  if not enabled cannot be clicked
for radio in radio_buttons:
    if radio.is_enabled():
        driver.execute_script(
            "arguments[0].click();",
            radio
        )
        break # Exit the current loop immediately,works with both for loops and while loops
###########################################################
print()
print("after click: button is selected or not:")
# Verify selected
for i, radio in enumerate(radio_buttons, start=1):
    print(f"Radio{i}: {radio.is_selected()}")
# Wait for result message
message = wait.until(
    EC.visibility_of_element_located(
        (By.CLASS_NAME, "text-success")
    )
)
print()
print("Was the selection successful?", message.text)
print()
assert message.text == "Yes"
   
time.sleep(10) 

driver.quit()