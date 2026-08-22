from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.set_window_size(1400, 900)
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = driver.find_element(By.ID, "dropdown") # WebElement
dropdown = Select(dropdown_element)  #Convert the WebElement to a Select wrapper object  
#test option 0: "Please select an option"
selected_option = dropdown.first_selected_option #select_option is WebElement
if selected_option.text == "Please select an option":
    print("PASS - Option 0: Please select an option")
else:
    print("FAIL - Option 0")
#all web elements 
all_options = dropdown.options
for option in all_options:
    print(type(option))

#test the 2 active options
for option_text in ["Option 1", "Option 2"]:

    dropdown.select_by_visible_text(option_text) #stand alone, no return value  

    selected_option = dropdown.first_selected_option #returns the selected option

    if selected_option.text == option_text:
        print(f"PASS - {option_text}")
    else:
        print(f"FAIL - Expected {option_text}, got {selected_option.text}")7491input("Press Enter to close...")
driver.quit()