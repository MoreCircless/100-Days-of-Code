from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("man")
lname.send_keys("ucircles")
email.send_keys("asfjaslfj@oulok.eu")

sing_up = driver.find_element(By.XPATH, "/html/body/form/button")

sing_up.click()






# driver.close() # JUST CLOSE A TAB
# driver.quit() # Quit entire program
