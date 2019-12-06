
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

driver.maximize_window()

driver.implicitly_wait(10)

driver.find_element_by_name("userName").send_keys("mercury")

driver.find_element_by_name("password").send_keys("mercury")

wait=WebDriverWait(driver,10)

ele=wait.until(EC.element_to_be_clickable(By.name("login")))

ele.click()

driver.close()









