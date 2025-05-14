from selenium import webdriver
import time

# Launch Chrome
chrome_driver = webdriver.Chrome()
chrome_driver.get('https://gmail.com/')
time.sleep(2)

#Print title in chrome
print("Title in Chrome:", chrome_driver.title)

chrome_driver.implicitly_wait(25) # seconds


#Quit Chrome
chrome_driver.quit()

'''
Launch Firefox

firefox_driver = webdriver.Firefox()

firefox_driver.get("https://bstackdemo.com/")

print("Title in Firefox:", firefox_driver.title)

firefox_driver.quit()'''