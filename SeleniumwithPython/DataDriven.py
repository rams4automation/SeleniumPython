
from selenium import webdriver
import time
import os

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10)

driver.get("http://newtours.demoaut.com/")

path="C:\TestData\Python.xlsx"


