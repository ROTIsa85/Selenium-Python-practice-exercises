#This time we'll wait for something different: a change in the browser URL.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

# Wait until the URL contains "login"
wait.until(
    EC.url_contains("login")
)

print("Login URL detected")

driver.quit()