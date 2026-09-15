from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

original_window = driver.current_window_handle

print(f"Original window before click: {original_window}")
print(f"Title: {driver.title}")

assert driver.current_window_handle == original_window
assert driver.title == "The Internet"


# Click the link that opens the new window
driver.find_element(By.LINK_TEXT, "Click Here").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.number_of_windows_to_be(2))

print(f"Number of windows: {len(driver.window_handles)}")


# Switch to the new window
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break


# Verify new window
print(f"New window handle: {driver.current_window_handle}")
print(f"New window title: {driver.title}")
print(f"New window URL: {driver.current_url}")

assert driver.title == "New Window"

# Switch back to original window
driver.switch_to.window(original_window)

print(f"Returned to original window: {driver.current_window_handle}")
print(f"Title: {driver.title}")

assert driver.current_window_handle == original_window
assert driver.title == "The Internet"


driver.quit()