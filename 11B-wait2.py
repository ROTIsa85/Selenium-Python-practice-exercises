#version 2 explicit wait: presence_of_element_located#
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

wait = WebDriverWait(driver, 10)

checkbox = wait.until(
    EC.presence_of_element_located(
        (By.ID, "checkbox")
    )
)

print("Checkbox found")

driver.quit()