
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
original_window = driver.current_window_handle
all_windows = driver.window_handles
if original_window in all_windows:
    print("PASS - Original window identified")
else:
    print("FAIL - Original window not found")
print(f"number of windows, {len(all_windows)}")
assert len(all_windows) == 1
driver.quit()