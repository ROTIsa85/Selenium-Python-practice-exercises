from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

print("Before click title:", driver.title)

driver.find_element(By.LINK_TEXT, "A/B Testing").click()

time.sleep(2)

print("After click title:", driver.title)
print("Current URL:", driver.current_url)

assert "/abtest" in driver.current_url

driver.quit()