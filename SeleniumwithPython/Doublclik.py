
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


driver=webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")

driver.implicitly_wait(10)

driver.get("https://artoftesting.com/sampleSiteForSelenium")

driver.maximize_window()

time.sleep(5)

dblElement=driver.find_element_by_id("dblClkBtn")

action=ActionChains(driver)

action.double_click(dblElement).perform()

time.sleep(5)

driver.quit()

