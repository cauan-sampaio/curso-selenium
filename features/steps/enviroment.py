from selenium import webdriver
from ipdb import set_trace
from ipdb import post_mortem

class Environment():
    def before_all(context):
        context.browser = webdriver.Firefox()

    def after_all(context):
        context.browser.quit()
    
    def after_step(context, step):
        if step.status == 'failed':
            set_trace()  # Inicia sessão interativa de depuração
            post_mortem(step.exc_traceback)  # Entra no modo de depuração pós-morte
