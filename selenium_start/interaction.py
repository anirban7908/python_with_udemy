from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome open after programme finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#open chrome browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# click on a item
active_editors = driver.find_element(By.ID, "mwDw")
# active_editors.click() #click happens here

# alternrive way to click LINK_TEXT
community_portal = driver.find_element(By.LINK_TEXT, "Community portal")
# community_portal.click()

# Sending keyboard inputs to selenium
search = driver.find_element(By.NAME, value="search")
print(search)
search.send_keys("Python", Keys.ENTER)
