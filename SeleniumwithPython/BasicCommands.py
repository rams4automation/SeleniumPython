
from selenium import webdriver
import time


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.maximize_window()

pagetitle=driver.title

print(pagetitle)

Pageurl=driver.current_url

print(Pageurl)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

driver.close()

driver.quit()