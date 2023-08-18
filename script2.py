from selenium import webdriver
from selenium.webdriver.common.by import By

# Recupere a instância existente do driver criada no script 1
from script1 import driver

# Execute ações no script 2 usando a mesma instância do driver
oi = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]')
oi.click()
oi.send_keys('korn')

# ... faça outras ações ...

# Não feche o driver do Selenium no final do script 2
