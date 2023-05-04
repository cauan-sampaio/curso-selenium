from selenium import webdriver
from time import sleep 

driver = webdriver.Firefox()
driver.get('https://github.com/cauan-sampaio')
sleep(3)
driver.switch_to.new_window('tab')
driver.get('https://github.com/cauan-sampaio?tab=repositories')
sleep(3)
driver.switch_to.new_window('tab')
driver.get('https://github.com/cauan-sampaio/curso-selenium')
sleep(3)
driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/watch?v=jR88BgYMlbQ&t=3164s')
sleep(3)
driver.switch_to.new_window('tab')
driver.get('https://www.youtube.com/watch?v=eQLRkeKOjE4&t=11593s')
sleep(3)
driver.current_url

def encontra_janela(palavra: str) -> bool:
    windows = driver.window_handles 
    for win in windows:
        driver.switch_to.window(win)
        if palavra in driver.current_url:
            print(f'Encontrei a janela {driver.current_url}')
            return True
    print(f'Não encontrei nenuma janela com a palavra: {palavra}')
    return False
encontra_janela('cauan-sampaio/curso-selenium')
sleep(10)
driver.quit()