

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

# -------------------------------------------------
# LOCATE THE DROP-DOWN
# -------------------------------------------------
dropdown = driver.find_element(
    By.ID,
    "mySelect"
)
# -------------------------------------------------
# CREATE SELECT OBJECT
# -------------------------------------------------
select = Select(dropdown)
# -------------------------------------------------
# SELECT AN OPTION & VERIFY THE SELECTION
# -------------------------------------------------
#1a#
select.select_by_visible_text("Set to 50%")
selected_option = select.first_selected_option
assert selected_option.text == "Set to 50%"
if selected_option.text == "Set to 50%":
   print(f"option text: {selected_option.text}")
#1b#
select.select_by_value("50%")
selected_option = select.first_selected_option
assert selected_option.text == "Set to 50%"
if selected_option.text == "Set to 50%":
    print(f"option value: 50%")    
#1C#
select.select_by_index(1)
selected_option = select.first_selected_option
assert selected_option.text == "Set to 50%"
if selected_option.text == "Set to 50%":
    print("option index: 1")    
#2#
select.select_by_value("25%")
selected_option = select.first_selected_option
assert selected_option.text == "Set to 25%"
if selected_option.text == "Set to 25%":
    print(f"option text: {selected_option.text}")
#3#
select.select_by_index(2)
selected_option = select.first_selected_option
assert selected_option.text == "Set to 75%"
if selected_option.text == "Set to 75%":
    print(f"option text: {selected_option.text}")
# -------------------------------------------------
# FINISH
# -------------------------------------------------
time.sleep(10)
driver.quit()