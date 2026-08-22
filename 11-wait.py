from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/login")

# Username
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# Password
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# Login button
login_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")
    )
)

login_button.click()

# Wait until the success message is visible
message_element = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

# Read the message
message_text = message_element.text

print(message_text)

# Verify success message
assert "You logged into a secure area!" in message_text

# Verify URL
assert "secure" in driver.current_url
time.sleep(10)
driver.quit()