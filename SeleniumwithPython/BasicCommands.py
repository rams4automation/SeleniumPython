
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.maximize_window()

Pagetitle=driver.title

print(Pagetitle)

Pageurl=driver.current_url

print(Pageurl)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(9)

##driver.close()       ## close only on browser which is focused browser

driver.quit()