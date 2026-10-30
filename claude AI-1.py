"""
Selenium test script for saucedemo.com login flow.
 
Covers 6 verification cases:
1. Valid login
2. Invalid username
3. Invalid password
4. Both fields empty
5. Locked-out user
6. Logout verification
 
Requirements:
    pip install selenium
    (uses Chrome WebDriver - make sure chromedriver is installed and on PATH,
     or install webdriver-manager: pip install webdriver-manager)
"""
 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
URL = "https://www.saucedemo.com/"
 
# ---- Locators ----
USERNAME_FIELD = (By.ID, "user-name")
PASSWORD_FIELD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")
ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
INVENTORY_TITLE = (By.CLASS_NAME, "title")
MENU_BUTTON = (By.ID, "react-burger-menu-btn")
LOGOUT_LINK = (By.ID, "logout_sidebar_link")
 
WAIT_TIMEOUT = 10
 
 
def get_driver():
    """Create and return a fresh Chrome WebDriver instance."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver
 
 
def login(driver, username, password):
    """Perform a login attempt with the given credentials."""
    driver.get(URL)
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
 
    username_field = wait.until(EC.visibility_of_element_located(USERNAME_FIELD))
    username_field.clear()
    username_field.send_keys(username)
 
    password_field = driver.find_element(*PASSWORD_FIELD)
    password_field.clear()
    password_field.send_keys(password)
 
    driver.find_element(*LOGIN_BUTTON).click()
 
 
def get_error_text(driver):
    """Wait for and return the error message text, or None if it never appears."""
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    try:
        error_element = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        return error_element.text
    except TimeoutException:
        return None
 
 
# ---- Test Case 1: Valid login ----
def test_valid_login():
    driver = get_driver()
    try:
        login(driver, "standard_user", "secret_sauce")
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        title_element = wait.until(EC.visibility_of_element_located(INVENTORY_TITLE))
 
        assert "inventory.html" in driver.current_url, \
            f"Expected inventory page, got {driver.current_url}"
        assert title_element.text == "Products", \
            f"Expected 'Products' title, got '{title_element.text}'"
        print("PASS: test_valid_login")
    finally:
        driver.quit()
 
 
# ---- Test Case 2: Invalid username ----
def test_invalid_username():
    driver = get_driver()
    try:
        login(driver, "not_a_real_user", "secret_sauce")
        error_text = get_error_text(driver)
        assert error_text is not None, "Expected an error message, got none"
        assert "do not match" in error_text.lower() or "not match" in error_text.lower(), \
            f"Unexpected error text: '{error_text}'"
        print("PASS: test_invalid_username")
    finally:
        driver.quit()
 
 
# ---- Test Case 3: Invalid password ----
def test_invalid_password():
    driver = get_driver()
    try:
        login(driver, "standard_user", "wrong_password")
        error_text = get_error_text(driver)
        assert error_text is not None, "Expected an error message, got none"
        assert "do not match" in error_text.lower() or "not match" in error_text.lower(), \
            f"Unexpected error text: '{error_text}'"
        print("PASS: test_invalid_password")
    finally:
        driver.quit()
 
 
# ---- Test Case 4: Both fields empty ----
def test_empty_fields():
    driver = get_driver()
    try:
        login(driver, "", "")
        error_text = get_error_text(driver)
        assert error_text is not None, "Expected an error message, got none"
        assert "username is required" in error_text.lower(), \
            f"Unexpected error text: '{error_text}'"
        print("PASS: test_empty_fields")
    finally:
        driver.quit()
 
 
# ---- Test Case 5: Locked-out user ----
def test_locked_out_user():
    driver = get_driver()
    try:
        login(driver, "locked_out_user", "secret_sauce")
        error_text = get_error_text(driver)
        assert error_text is not None, "Expected an error message, got none"
        assert "locked out" in error_text.lower(), \
            f"Unexpected error text: '{error_text}'"
        print("PASS: test_locked_out_user")
    finally:
        driver.quit()
 
 
# ---- Test Case 6: Logout verification ----
def test_logout():
    driver = get_driver()
    try:
        # First log in successfully
        login(driver, "standard_user", "secret_sauce")
        wait = WebDriverWait(driver, WAIT_TIMEOUT)
        wait.until(EC.visibility_of_element_located(INVENTORY_TITLE))
 
        # Open the side menu
        menu_button = wait.until(EC.element_to_be_clickable(MENU_BUTTON))
        menu_button.click()
 
        # Click Logout once the link is clickable (menu slides in)
        logout_link = wait.until(EC.element_to_be_clickable(LOGOUT_LINK))
        logout_link.click()
 
        # Verify we're back on the login page
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON))
        assert driver.current_url == URL, \
            f"Expected to be back at {URL}, got {driver.current_url}"
        print("PASS: test_logout")
    finally:
        driver.quit()
 
 
if __name__ == "__main__":
    test_valid_login()
    input("Press Enter to continue...")
    test_invalid_username()
    input("Press Enter to continue...")
    test_invalid_password()
    input("Press Enter to continue...")
    test_empty_fields()
    input("Press Enter to continue...")
    test_locked_out_user()
    input("Press Enter to continue...")
    test_logout()
    input("Press Enter to continue...")
    print("\nAll tests completed.")
    