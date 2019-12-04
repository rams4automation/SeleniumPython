
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(5)

driver.switch_to_alert().accept()

time.sleep(5)

driver.close()