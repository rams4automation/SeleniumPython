
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

driver.maximize_window()

driver.implicitly_wait(10)

element=driver.find_element_by_id("select-demo")

drpdwn=Select(element)

time.sleep(5)

drpdwn.select_by_value("Sunday")

time.sleep(5)

# ******* Count Number drop down Options

len1=len(drpdwn.options)

print(len1)

# Capture all the options and print them as a output

time.sleep(5)

all_options=drpdwn.options

for x in all_options:
    print(x.text)

time.sleep(5)

driver.close()


