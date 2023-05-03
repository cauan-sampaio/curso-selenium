from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://omayo.blogspot.com/")
sleep(3)
prompt = driver.find_element(By.ID, "prompt")
sleep(3)
prompt.click()


