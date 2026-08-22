
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open Chrome
driver = webdriver.Chrome()

# Open page
driver.get("https://testautomationpractice.blogspot.com/")

# Find Name field
name_box = driver.find_element(By.ID, "name")

# Type a name
name_box.send_keys("ILAN")

# Read the value back
value = name_box.get_attribute("value")
print("Name field contains:", value)
assert value.startswith("IL")
assert "IL" in value
time.sleep(15)
name_box.clear() 
value = name_box.get_attribute("value")
print(f"line25 {value}")
assert value == ""
placeholder = name_box.get_attribute("placeholder")
print(f"line28:Placeholder {placeholder}")
assert placeholder == "Enter Name"
assert "Name" in placeholder
email_box = driver.find_element(By.ID, "email")
email_box.send_keys("ilan@hotmail.com")
value = email_box.get_attribute("value")
assert value == "ilan@hotmail.com"
assert "@" in value
assert "@hotmail" in value
assert value.startswith("ilan")
assert value.endswith(".com")
print("email field contains:", value)

# Pause so you can see the result
time.sleep(15)

# Close browser
driver.quit()