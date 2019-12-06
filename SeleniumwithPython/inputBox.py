
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("https://www.toolsqa.com/automation-practice-form/")

driver.implicitly_wait(10)

driver.maximize_window()

driver.find_element_by_id("cookie_action_close_header").click()

time.sleep(5)

inputboxes=driver.find_elements_by_class_name("control-group")

print(len(inputboxes))

time.sleep(5)

driver.close()