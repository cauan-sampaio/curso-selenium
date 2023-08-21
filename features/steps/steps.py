from selenium import webdriver
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.keys import Keys
from json import loads
from selenium.webdriver.common.by import By

class Page:
    @given('Que eu esteja na página')
    def go_to_page(context):
        context.browser = webdriver.Firefox()
        context.browser.get("https://omayo.blogspot.com/")
        sleep(3)
class Login(Page):
    @when('Quando eu clickar nos inputs de user-name e senha')
    def logar(context):
        texto_do_step = loads(context.text)
        username = context.browser.find_element(By.NAME, "userid")
        username.send_keys(texto_do_step['nome'])
        sleep(3)
        password = context.browser.find_element(By.NAME, "pswrd")
        password.send_keys(texto_do_step['senha'])
        sleep(3)
    @then('O usuário poderá logar!')
    def entrar(context):
        login = context.browser.find_element(By.CSS_SELECTOR, '#HTML42 > div:nth-child(2) > form:nth-child(2) > input:nth-child(3)')
        login.click()
        sleep(3)