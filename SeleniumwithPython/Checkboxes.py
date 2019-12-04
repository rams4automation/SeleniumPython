
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.get("https://www.toolsqa.com/automation-practice-form/")

driver.find_element_by_id("cookie_action_close_header").click()

time.sleep(5)

status=driver.find_element_by_id("profession-0").is_selected()

print(status)

time.sleep(5)

if status == False:
    print("Check box is not Selected")
    driver.find_element_by_id("profession-0").click()
else:
    print("Check box is Selected")

time.sleep(5)

status=driver.find_element_by_id("profession-0").is_selected()

print(status)

driver.close()
