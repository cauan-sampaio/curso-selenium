from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://selenium.dunossauro.live/exercicio_06.html?nome=n%C3%A3o&senha=nao&l1c0=Enviar%21#")
sleep(3)
while True:
        spans = driver.find_element(By.TAG_NAME, "span")
        if spans.text == "l0c0":
            xpath_form0 = driver.find_element(By.CLASS_NAME, "form-l0c0")
            xpath_name0 = xpath_form0.find_element(By.NAME,"nome" )
            xpath_name0.send_keys("oi")
            xpath_password0 = xpath_form0.find_element(By.NAME, "senha")
            xpath_password0.send_keys("1")
            enviar0 = xpath_form0.find_element(By.NAME, "l0c0")
            enviar0.click()
            sleep(3)
        elif spans.text == "l0c1":    
            xpath_form1 = driver.find_element(By.CLASS_NAME, "form-l0c1")
            xpath_name1 = xpath_form1.find_element(By.NAME,"nome" )
            xpath_name1.send_keys("oi")
            xpath_password1 = xpath_form1.find_element(By.NAME, "senha")
            xpath_password1.send_keys("1")
            enviar1 = xpath_form1.find_element(By.NAME, "l0c1")
            enviar1.click()
            sleep(3)
        elif spans.text == "l1c0":    
            xpath_form2 = driver.find_element(By.CLASS_NAME, "form-l1c0")
            xpath_name2 = xpath_form2.find_element(By.NAME,"nome" )
            xpath_name2.send_keys("oi")
            xpath_password2 = xpath_form2.find_element(By.NAME, "senha")
            xpath_password2.send_keys("1")
            enviar2 = xpath_form2.find_element(By.NAME, "l1c0")
            enviar2.click()
            sleep(3)
        elif spans.text == "l1c1":
            xpath_form3 = driver.find_element(By.CLASS_NAME, "form-l1c1")
            xpath_name3 = xpath_form3.find_element(By.NAME,"nome" )
            xpath_name3.send_keys("oi")
            xpath_password3 = xpath_form3.find_element(By.NAME, "senha")
            xpath_password3.send_keys("1")
            enviar3 = xpath_form3.find_element(By.NAME, "l1c1")
            enviar3.click()
