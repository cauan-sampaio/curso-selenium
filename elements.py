from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://www.google.com/")
search = driver.find_element(By.ID, "APjFqb")
search.send_keys("some text")
search.send_keys(" and some", Keys.ENTER)
search.clear()