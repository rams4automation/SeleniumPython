
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.implicitly_wait(10)

time.sleep(5)

driver.switch_to.frame(0)

path="C://Python//Homepage.jpg"

time.sleep(5)

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-11']").send_keys(path)
