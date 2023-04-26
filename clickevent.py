from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
from time import sleep
driver.get("https://curso-python-selenium.netlify.app/aula_03.html")
sleep(3)
a = driver.find_element(By.ID,"ancora")
a.click()
print(f'texto de a: {a.text}')
