from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#############################
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
#############################
username_element = driver.find_element(By.ID, "username")
username_element.send_keys("tomsmith")
username_text = username_element.get_attribute("value")
print("UserName:", username_text)
assert "smit" in username_text
############################
password_element = driver.find_element(By.ID, "password")
password_element.send_keys("SuperSecretPassword!")
time.sleep(15)
password_text = password_element.get_attribute("value")
print("Password:", password_text)
assert "SuperSecretPassword!" in password_text
############################
login_element = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_element.click()
print(driver.current_url)
print(driver.title)
############################
message_element = driver.find_element(By.ID, "flash")
message_text = message_element.text
print(message_text)
assert "You logged into a secure area!" in message_text
############################
time.sleep(10)
driver.quit()
