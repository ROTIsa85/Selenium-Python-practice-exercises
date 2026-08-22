from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

#driver.get("https://the-internet.herokuapp.com/checkboxes")
#driver.get("https://rahulshettyacademy.com/AutomationPractice/?utm_source=chatgpt.com")
driver.get("https://seleniumbase.io/demo_page")
# -------------------------------------------------
# LOCATE ALL CHECKBOXES
# -------------------------------------------------

checkboxes = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

# Example:
# If there are 5 checkboxes:
#
# Python index:       0       1       2       3    4
# Checkbox:          [0]     [1]     [2]     [3]  [4]
#
# len(checkboxes) = 5

#Main checkboxes:
#Index 0 → CheckBox
#Index 1 → CheckBoxes
#Index 2 → CheckBoxes
#Index 3 → CheckBoxes
#Index 4 → Pre-Check Box

#Total = 5
# -------------------------------------------------
# SEQUENCE 1
# SELECT EVERY CHECKBOX ONE BY ONE
# -------------------------------------------------

# First make sure ALL checkboxes are unselected.
## We do this because we want a known starting state:
#
# Index:       0    1    2    3 4
# State:       0    0    0    0 0
#
# 0 = not selected
# 1 = selected

for checkbox in checkboxes:

    if checkbox.is_selected():
        checkbox.click()


# Verify that ALL checkboxes are now unselected.

for checkbox in checkboxes:

    assert not checkbox.is_selected()

print(len(checkboxes))
# -------------------------------------------------
# SELECT CHECKBOXES ONE BY ONE
# -------------------------------------------------

for i in range(len(checkboxes)):

    # i will be:
    #
    # 0 → Checkbox 0
    # 1 → Checkbox 1
    # 2 → Checkbox 2
    # 3 → Checkbox 3
    # if there are 4 checkboxes.

    checkboxes[i].click()

    time.sleep(5)
    # ---------------------------------------------
    # VERIFY THE STATE OF ALL CHECKBOXES
    # ---------------------------------------------

    for j in range(len(checkboxes)):

        # j is the checkbox we are currently verifying.
        #
        # i = checkbox we just clicked
        # j = checkbox we are checking


        if j <= i:

            # All indexes from 0 through i
            # should now be selected.

            assert checkboxes[j].is_selected()
        else:

            # All indexes greater than i
            # should still be unselected.

            assert not checkboxes[j].is_selected()


# At the end of this sequence:
#
# Index:       0    1    2    3
# State:       1    1    1    1
#
# All checkboxes are selected.


# -------------------------------------------------
# SEQUENCE 2
# UNSELECT EVERY CHECKBOX ONE BY ONE
# -------------------------------------------------

# First verify that all checkboxes are selected.

for checkbox in checkboxes:

    assert checkbox.is_selected()


# -------------------------------------------------
# UNSELECT CHECKBOXES ONE BY ONE
# -------------------------------------------------

for i in range(len(checkboxes)):

    # i will again be:
    #
    # 0 → Checkbox 0
    # 1 → Checkbox 1
    # 2 → Checkbox 2
    # 3 → Checkbox 3
    checkboxes[i].click()


    # ---------------------------------------------
    # VERIFY THE STATE OF ALL CHECKBOXES
    # ---------------------------------------------

    for j in range(len(checkboxes)):

        # j = checkbox currently being verified


        if j <= i:

            # All indexes from 0 through i
            # should now be unselected.

            assert not checkboxes[j].is_selected()

        else:

            # All indexes greater than i
            # should still be selected.

            assert checkboxes[j].is_selected()


# At the end of this sequence:
#
# Index:       0    1    2    3
# State:       0    0    0    0
#
# All checkboxes are unselected.


# -------------------------------------------------
# FINISH
# -------------------------------------------------
time.sleep(20)
driver.quit()