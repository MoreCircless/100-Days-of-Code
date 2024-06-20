from selenium import webdriver
import selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

element = driver.find_element(by=By.NAME, "medium-widget event-widget last")
print(element.text)


driver.fin


# driver.close()
driver.quit()





