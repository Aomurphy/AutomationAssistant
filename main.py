from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome
url = 'https://gmail.com/'
driver = webdriver.Chrome()
username = 'bunnyboo1717'

driver.get(url)
time.sleep(1)
driver.implicitly_wait(25) # seconds
driver.find_element(By.ID,'identifierId').send_keys(username)
time.sleep(1)
driver.find_element(By.ID,'identifierNext').click()
time.sleep(5)

#Print title in chrome
print("Title in Chrome:", driver.title)

#driver.implicitly_wait(25) # seconds


#Quit Chrome
#chrome_driver.quit()

'''
Launch Firefox

firefox_driver = webdriver.Firefox()

firefox_driver.get("https://bstackdemo.com/")

print("Title in Firefox:", firefox_driver.title)

firefox_driver.quit()'''