from selenium import webdriver

# Launch Chrome

chrome_driver = webdriver.Chrome()

chrome_driver.get('https://bstackdemo.com/')

print("Title in Chrome:", chrome_driver.title)

chrome_driver.quit()

# Launch Firefox

firefox_driver = webdriver.Firefox()

firefox_driver.get("https://bstackdemo.com/")

print("Title in Firefox:", firefox_driver.title)

firefox_driver.quit()