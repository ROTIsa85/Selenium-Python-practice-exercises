from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

driver.find_element(By.LINK_TEXT, "A/B Testing").click()

time.sleep(10)

heading = driver.find_element(By.TAG_NAME, "h3").text

print("Page Heading:", heading)

driver.quit()