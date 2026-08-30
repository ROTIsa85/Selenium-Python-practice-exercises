#Exercise 11B6 — Explicit Wait: title_is

#This teaches you that an explicit wait doesn't have to be about an element. You can wait for a page condition.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")

wait = WebDriverWait(driver, 10)

# Wait until the page title is exactly as expected
wait.until(
    EC.title_is("The Internet")
)

print("Page title is correct")

driver.quit()