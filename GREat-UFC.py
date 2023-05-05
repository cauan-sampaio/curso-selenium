from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://testlink.org/")
print(driver.current_url)
assert "https://testlink.org/" in driver.current_url
git = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/a[3]")
git.click()
print(driver.current_url)
assert "https://github.com/TestLinkOpenSourceTRMS/testlink-code/tree/testlink_1_9_20_fixed/" in driver.current_url
sleep(3)
searchGit = driver.find_element(By.CSS_SELECTOR, ".js-site-search-focus")
sleep(3)
searchGit.send_keys('oi')
searchGit.send_keys(Keys.ENTER)




