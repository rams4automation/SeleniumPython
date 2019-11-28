from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")
driver.get("https://www.jetbrains.com/education/download/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()