import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

headOption = webdriver.FirefoxOptions()
headOptions.**add_argument('-headless')**

driver = webdriver.Firefox(**options**=headOptions, executable_path=r'C:\Users\bayme\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe')
driver = webdriver.Firefox()
driver.get("https://inspirobot.me/")#put here the adress of your page
elem = driver.find_elements_by_xpath('//*[@id="top"]/div[1]/div[2]/div')#put here the content you have put in Notepad, ie the XPath
elem[0].click()
time.sleep(3)
img = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/img')
src = img.get_attribute('src')
print(src)
driver.close()
