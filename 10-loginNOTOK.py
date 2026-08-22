from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")

# Username
username_element = driver.find_element(By.ID, "username")
username_element.send_keys("Tomsmith")

# Password
password_element = driver.find_element(By.ID, "password")
password_element.send_keys("superSecretPassword!")
time.sleep(10)
# Login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(2)

# Verify URL
print(driver.current_url)

assert "secure" not in driver.current_url

# Verify error message
message = driver.find_element(By.ID, "flash").text
assert "username is" in message
time.sleep(10)
driver.quit()
