from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

original_handle = driver.current_window_handle

print(f"Original window before click:, {original_handle} Title: {driver.title}")

driver.find_element(By.LINK_TEXT, "Click Here").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))

for handle in driver.window_handles: 
    driver.switch_to.window(handle)
    if "New Window" in driver.current_url:
        assert handle != original_handle, "wrong window"     
driver.switch_to.window(original_handle)
print(f"Returned to original window before clicking: {original_handle} Title: {driver.title}")

driver.quit()
    
