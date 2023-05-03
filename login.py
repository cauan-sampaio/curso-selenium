from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://omayo.blogspot.com/")
sleep(3)
username = driver.find_element(By.NAME, "userid")
username.send_keys("cauan")
sleep(3)
password = driver.find_element(By.NAME, "pswrd")
password.send_keys("123")
sleep(3)
login = driver.find_element(By.CSS_SELECTOR, '#HTML42 > div:nth-child(2) > form:nth-child(2) > input:nth-child(3)')
login.click()
sleep(3)