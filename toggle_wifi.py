from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("http://192.168.1.1/")
pwd = driver.find_element_by_id("INPUT_Psd")
pwd.clear() #cleared any data that was pre filled
pwd.send_keys("admin") #entered the pass
pwd.send_keys(Keys.RETURN) #pressed enter

driver.get("http://192.168.1.1/cgi-bin/webproc?getpage=html/index.html&var:menu=setup&var:page=wireless&var:subpage=wlbasic") #go to the wireless page

checkbox = driver.find_element_by_id("INPUT_Enable") # select the enable/disable checkbox
checkbox.click() # click the enable disable check box
submit = driver.find_element_by_id("Apply") # select the submit button to apply changes
submit.click() # click the Apply button to make changes
driver.close()



