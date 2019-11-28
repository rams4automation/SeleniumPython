from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\Selenium\chromedriver.exe")

driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)

print(driver.current_url)

time.sleep(5)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(9)

driver.close()

##driver.quit()
