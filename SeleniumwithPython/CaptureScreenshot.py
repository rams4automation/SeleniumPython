from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

driver.implicitly_wait(10)

driver.get_screenshot_as_file("C://Python//Homepage.png")

driver.close()
