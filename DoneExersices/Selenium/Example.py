from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
data = driver.find_element(By.ID, "success-story-1180")
print(data.text)








# driver.close() # JUST CLOSE A TAB
driver.quit() # Quit entire program





