from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.ID, "articlecount")
number = number.text
number = number.split(" ")
print(number[0])







# driver.close() # JUST CLOSE A TAB
driver.quit() # Quit entire program

