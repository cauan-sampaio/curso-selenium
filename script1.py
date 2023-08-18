from selenium import webdriver

# Inicie o driver do Selenium
driver = webdriver.Firefox()

# Execute ações no script 1
driver.get("https://www.google.com")
# ... faça outras ações ...

# Não feche o driver do Selenium no final do script 1
