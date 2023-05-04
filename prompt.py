from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait as WDW
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from time import sleep
driver = webdriver.Firefox()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
wdw = WDW(driver, 10)
prompt = wdw.until(visibility_of_element_located((By.ID, "prompt")), 'Oi')
sleep(2)
prompt.click()
sleep(2)
alert = Alert(driver)
sleep(2)
alert.send_keys('alguma coisa')
sleep(2)
alert.accept
print('passou')
driver.quit()

