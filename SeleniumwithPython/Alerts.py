
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.implicitly_wait(10)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

##driver.switch_to_alert().accept()

alert=driver.switch_to_alert()

alert.accept()

#alert.dismiss()

time.sleep(5)

driver.close()