from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.switch_to.new_window("tab")
new_window = driver.current_window_handle
all_windows = driver.window_handles
if new_window in all_windows:
    print("PASS - NEW window identified")
else:
    print("FAIL - NEW window not found")
print(f"number of windows, {len(all_windows)}")
assert len(all_windows) == 2
driver.quit()