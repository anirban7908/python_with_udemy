from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

fname.send_keys('Anirban')
lname.send_keys('Choudhury')
email.send_keys('anirban.text@gmail.com')

submit = driver.find_element(By.CSS_SELECTOR, 'form button')
submit.click()