from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"""
Tarefa de casa: Implemente a classe SeleniumPage
de forma que ela fique responsável pelos comandos 
do selenium, como o find_element e o send_keys
"""

class SeleniumPage:
    def __init__(self, driver):
        self.driver = driver
        def encontrar_elementos(self, by, value):
            return self.driver.find_element(by, value)
        def encontrar_chaves(self, element, texto):
            element.send_keys(texto)


class SauceDemoPage:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
        self.url = 'https://www.saucedemo.com/'

    def entrar(self) -> None:
        self.driver.get(self.url)

    def get_titulo(self):
        return self.driver.find_element(By.CLASS_NAME, "login_logo").text
    
class CaixaLogin(SauceDemoPage):
    def __init__(self, nome, senha) -> None:
        super().__init__()
        self.nome = nome
        self.senha = senha

    def escrever_nome(self):
        nome = self.driver.find_element(By.ID, "user-name")
        nome.send_keys(self.nome)

    def escrever_senha(self):
        senha = self.driver.find_element(By.ID, "password")
        senha.send_keys(self.senha)
    
    def submit(self):
        botao = self.driver.find_element(By.ID, "login-button")
        botao.click()

    # def submit()

pagina = CaixaLogin("standard_user", "secret_sauce")
pagina.entrar()

pagina.escrever_nome()
pagina.escrever_senha()
pagina.submit()


sleep(5)