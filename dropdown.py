from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
# SELECT AN OPTION
# -------------------------------------------------

select.select_by_visible_text("Set to 50%")


# -------------------------------------------------
# VERIFY THE SELECTION
# -------------------------------------------------

selected_option = select.first_selected_option

assert selected_option.text == "Set to 50%"


# -------------------------------------------------
# FINISH
# -------------------------------------------------

driver.quit()