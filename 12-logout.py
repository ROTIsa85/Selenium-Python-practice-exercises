from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome
driver = webdriver.Chrome()

# Create an explicit wait
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://the-internet.herokuapp.com/login")

# Enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# Enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click Login
driver.find_element(
    By.CSS_SELECTOR,
    "button[type='submit']"
).click()

# Wait for successful LOGIN
success_message = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

# Read and verify the success message
print("line34 in login:", success_message.text)
print("line 35 in login:", driver.current_url)

assert "You logged into a secure area!" in success_message.text

# Verify the URL
assert "secure" in driver.current_url

# -------------------------
# Logout
# -------------------------
logout_button = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "a.button")
    )                                       
) #above locator is the best for logout
# Wait until the Logout link is clickable
#above: can use also By.CSS_SELECTOR, "a[href='/logout']"
# Click LOGOUT
logout_button.click()

# Wait until the login page appears again
wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)
# DO NOT VERIFY TEXT OH INPUT USERR NAME ELEMENT!!!!!!!!!!!
# Verify the URL
print("line 58 in logout:", driver.current_url)

assert "login" in driver.current_url

# Wait for the logout message
logout_message = wait.until(
    EC.visibility_of_element_located((By.ID, "flash"))
)

# Read and verify the logout message
print("line 68 in logout:", logout_message.text)

assert "You logged out of the secure area!" in logout_message.text
time.sleep(20)
# Close the browser
driver.quit()