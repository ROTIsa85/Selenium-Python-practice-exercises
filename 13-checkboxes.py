from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='checkbox']") # see also "button[type='submit'] for login
print(len(checkboxes))
assert (len(checkboxes)) == 2
print("checkbox1:", checkboxes[0])
print("checkbox2:", checkboxes[1])
print("Checkbox 1:", checkboxes[0].is_selected())
print("Checkbox 2:", checkboxes[1].is_selected())
if not checkboxes[0].is_selected():
    print("checkbox 1 is not selected")
if checkboxes[1].is_selected():
    print("line 26: checkbox 2 is selected")   
time.sleep(10)   
# Click the first checkbox
checkboxes[0].click()
print("Line 30 Checkbox 1:", checkboxes[0].is_selected())
assert checkboxes[0].is_selected()
checkboxes[1].click()
print("Checkbox 2:", checkboxes[1].is_selected())
assert not checkboxes[1].is_selected()
time.sleep(20)
driver.quit()