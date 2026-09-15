from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
first_window = driver.current_window_handle
driver.switch_to.new_window ("tab") 
second_window = driver.current_window_handle
all_windows = driver.window_handles
if second_window in all_windows:
    print("Second window identified") 
else:
    print("Second window not found")   
    
driver.switch_to.window(first_window)
assert driver.current_window_handle == first_window, "FAIL - First window not found " 
print(all_windows)
driver.quit()