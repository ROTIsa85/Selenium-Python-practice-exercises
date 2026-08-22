from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

# -------------------------------------------------
# LOCATE ALL RADIO BUTTONS
# -------------------------------------------------

radios = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='radio']"
)

# Example:
#
# Python index:       0       1
# Radio button:      [0]     [1]
#
# Radio 0 = radioButton1
# Radio 1 = radioButton2


# -------------------------------------------------
# VERIFY INITIAL STATE
# -------------------------------------------------

# Radio 0 should initially be selected.
# Radio 1 should initially be unselected.

assert radios[0].is_selected()
assert not radios[1].is_selected()


# -------------------------------------------------
# SEQUENCE 1
# SELECT RADIO BUTTON 1
# -------------------------------------------------

radios[1].click()


# Expected state:
#
# Index:       0    1
# State:       0    1
## Radio 1 is selected.
# Radio 0 is automatically unselected.


# Verify the state.

assert not radios[0].is_selected()
assert radios[1].is_selected()


# -------------------------------------------------
# SEQUENCE 2
# SELECT RADIO BUTTON 0
# -------------------------------------------------

radios[0].click()


# Expected state:
#
# Index:       0    1
# State:       1    0
#
# Radio 0 is selected.
# Radio 1 is automatically unselected.


# Verify the state.
assert radios[0].is_selected()
assert not radios[1].is_selected()


# -------------------------------------------------
# FINISH
# -------------------------------------------------

driver.quit()
