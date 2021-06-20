from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

print('Selenium Easy Demo' in chrome_browser.title)

chrome_browser.close()
