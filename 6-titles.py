from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.LINK_TEXT, "A/B Testing").click() #link tag <a>
title = driver.title
print (f"line9 driver type, {(type(title))}")
print("line10 Page title:", title)
assert "The Internet" in title
heading = driver.find_element(By.TAG_NAME, "h3").text 
print(f"line13 heading {type(heading)}")
print (f"line14 {heading}")
time.sleep(10)
driver.quit()