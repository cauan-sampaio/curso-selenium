from selenium import webdriver

# Inicie o driver do Selenium
driver = webdriver.Chrome()

# Execute ações no script 1
driver.get("https://www.example.com")
# ... faça outras ações ...

# Não feche o driver do Selenium no final do script 1
