from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\Daniel G\Downloads\geckodriver.exe')

driver.get("https://www.bloomberg.com/markets/currencies")