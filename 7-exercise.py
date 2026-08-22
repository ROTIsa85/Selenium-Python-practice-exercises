#SUBJECT: driver.find_elements
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
listx = driver.find_elements(By.TAG_NAME, "a")
print("First link:", repr(listx[0].text))
assert "A/B" in (listx[1].text)
for i, link in enumerate(listx[:5]): # enumerate(names): gives position like 1., 2.
    print(i, repr(link.text))
time.sleep(2)
for link in listx:
    print(link.text)
print("type", type(listx))
print("length list", len(listx))
print("Number of links:", len(listx))

all_links = [link.text for link in listx]  # !!find the string in any of the links!!
assert "A/B Testing" in all_links

time.sleep(10)
driver.quit()