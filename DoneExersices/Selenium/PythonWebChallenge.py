from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
date_list = []
name_list = []
for item in date:
    date_list.append(item.text)
for item in name:
    name_list.append(item.text)
dictonary = {}
for n in range(5):
    templist = []
    templist.append(date_list[n])
    templist.append(name_list[n])
    dictonary[n] = templist

print(dictonary)



driver.quit() 


