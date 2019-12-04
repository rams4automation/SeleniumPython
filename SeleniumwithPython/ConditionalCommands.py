
from selenium import webdriver

import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.maximize_window()

UserEle=driver.find_element_by_name("userName")

print(UserEle.is_displayed())

print(UserEle.is_enabled())

time.sleep(10)

PwdeEle=driver.find_element_by_name("password")

print(PwdeEle.is_displayed())

print(PwdeEle.is_enabled())

UserEle.send_keys("mercury")
PwdeEle.send_keys("mercury")

driver.find_element_by_name("login").click()

time.sleep(5)

roundtripbutton=driver.find_element_by_name("tripType")

time.sleep(10)

print(roundtripbutton.is_selected())

driver.close()
