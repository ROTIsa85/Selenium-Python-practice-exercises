"""
Exercise 15 - Dropdown Lists

Objective:
Learn how to use Selenium's Select class of dropdown lists.

Topics learned:
- Locate a dropdown
- Select class (dropdown = Select(dropdown_element)
- Create a Select object
- options
- first_selected_option
- select_by_visible_text()
- get_attribute("value")
- Read the selected option
- Verify the result
- first_selected_option
- options
- select_by_visible_text()
- Verifying default selection
- Verification all active options
- outerHTML
- len(dropdown.options)
- Using a for loop to avoid duplicate code

Select class wraps the <select> WebElement and gives you convenient methods like:
-select_by_visible_text()
-select_by_value()
-options
code: dropdown = Select(dropdown_element) 

WebElement has properties and methods such as:
option.text
option.get_attribute("value")
option.is_enabled()
option.is_selected()
option.click()

dropdown = Select(dropdown_element)
Class: Select
Object (instance): dropdown
"""
########################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.set_window_size(1400, 900)
driver.get(
    "https://the-internet.herokuapp.com/dropdown")
print()
dropdown_element = driver.find_element(By.ID, "dropdown")
print("HTML:", dropdown_element.get_attribute("outerHTML"))
dropdown = Select(dropdown_element)  #Convert the dropdown WebElement to a Select object  
selected_option = dropdown.first_selected_option #selected_option is Web Element

#test the default option start 
if selected_option.text == "Please select an option":
    print(f"PASS - Default option is correct: {selected_option.text}" )
else:
    print("FAIL - Unexpected default option")
#test default option end
#print all web elements 
all_options = dropdown.options
for option in all_options:
    print(type(option))
    
#test all options atributes start 
all_options = dropdown.options
for option in all_options:
    print(option.get_attribute("value")) 
#options count 
print("options count:", len(dropdown.options))

#all options text 
for i, option in enumerate(all_options):
    print(f"Index {i}: {option.text}")
#

dropdown.select_by_visible_text("Option 1") # does not return value, only changes state of dropd.
selected_option = dropdown.first_selected_option
print(selected_option.text)

#
for option_text in ["Option 1", "Option 2"]:

    dropdown.select_by_visible_text(option_text) #no value returned 

    selected_option = dropdown.first_selected_option

    if selected_option.text == option_text:
        print(f"PASS: {option_text}")
    else:
        print(f"FAIL: Expected {option_text}, got {selected_option.text}")
#
time.sleep(20) 
driver.quit()