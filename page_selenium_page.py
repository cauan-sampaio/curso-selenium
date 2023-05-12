from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SeleniumPage:
    def __init__(self) -> None:
        self.webdriver = webdriver.Chrome()

    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def escrever(self, locator, str):
        self.encontrar_elemento(locator).send_keys(str)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

class SauceDemoPage(SeleniumPage):
    def __init__(self) -> None:
        super().__init__()
        self.driver = self.webdriver
        self.url = 'https://www.saucedemo.com/'

    def entrar(self) -> None:
        self.driver.get(self.url)

    def get_titulo(self):
        return self.encontrar_elemento((By.CLASS_NAME, "login_logo")).text
    
class CaixaLogin(SauceDemoPage):
    def __init__(self) -> None:
        super().__init__()
        self.nome = (By.ID, "user-name")
        self.senha = (By.ID, "password")
        self.botao = (By.ID, "login-button")

    def escrever_nome(self, nome_str: str):
        self.escrever(self.nome, nome_str)

    def escrever_senha(self, senha_str: str):
        self.escrever(self.senha, senha_str)
    
    def submit(self):
        self.clicar(self.botao)

    def logar(self, nome_user, senha_user):
        self.escrever_nome(nome_user)
        self.escrever_senha(senha_user)
        self.submit()

class Credenciais(SauceDemoPage):
    def __init__(self) -> None:
        super().__init__()
        self.usuarios = (By.XPATH, '//*[@id="login_credentials"]/br')
        pagina.driver.find_element(By.ID, "login_credentials").text
    def get_usuarios(self):
        string = pagina.driver.find_element(By.ID, "login_credentials").text
        vetor = string.split('\n')[1:]
        return vetor

    def get_senhas(self):
        string = pagina.driver.find_element(By.ID, "login_credentials").text
        vetor = string.split('\n')[1:]
        return vetor




pagina = CaixaLogin()
pagina.entrar()
print(pagina.get_titulo())
credenciais = Credenciais()
usuarios = credenciais.get_usuarios()
senhas = credenciais.get_senhas()

for usuario, senha in zip(usuarios, senhas):
    print("Usuário:", usuario)
    print("Senha:", senha)
    print("-------------------")

pagina.logar('standard_user', 'secret_sauce')



sleep(5)