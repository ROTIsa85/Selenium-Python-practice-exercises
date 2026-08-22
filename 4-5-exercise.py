from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()     #selenium

driver.get("https://the-internet.herokuapp.com/") 
title = driver.title 
print(driver.title)
print(f"line 11, {title}")
#Note: loading driver.get() waits for the complete page load
current_url = driver.current_url # https://the-internet.herokuapp.com
print("14 Current URL:", current_url)
print("hero" in current_url)
print("her0" in current_url)
assert "hero" in "https://the-internet.herokuapp.com"
print ("her0" in "https://the-internet.herokuapp.com")
driver.find_element(By.LINK_TEXT, "A/B Testing").click() 
#first find element <a href="/abtest">A/B Testing</a> followed by click()
current_url = driver.current_url
assert "abtest" in current_url  #https://the-internet.herokuapp.com/abtest
print("Line23 Current URL:", current_url) #https://the-internet.herokuapp.com/abtest
time.sleep(2)  #selenium

heading = driver.find_element(By.TAG_NAME, "h3").text 
print(type(heading))
assert "A/B Test" in heading 
print("Page Heading:", heading) #prints Page Heading: A/B Test Variation 1
heading_element = driver.find_element(By.TAG_NAME, "h3")
print(f"line 31 {driver.current_url}")
print(driver.title)
print (f"line 33, {heading_element.text}")
print(f"line34, {type(heading_element.tag_name)}")   
print(f"Line35, {heading_element.tag_name}") 
print(f"line36, {title}")
time.sleep(10)
driver.quit()