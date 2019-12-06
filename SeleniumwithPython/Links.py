
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("http://newtours.demoaut.com/")

links=driver.find_elements(By.TAG_NAME, "a")

print("Number of links:", len(links))

for link in links:
    print(link.text)

time.sleep(5)

driver.close()

