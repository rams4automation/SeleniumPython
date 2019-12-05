
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.implicitly_wait(10)

driver.maximize_window()

time.sleep(5)

source_ele=driver.find_element_by_xpath("//*[@id='box6']")
taget_ele=driver.find_element_by_xpath("//*[@id='box106']")

Action=ActionChains(driver)
Action.drag_and_drop(source_ele,taget_ele).perform()

time.sleep(5)

driver.close()