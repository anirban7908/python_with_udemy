from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after programme finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#open chrome browser
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

event_list = {}

# items = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

# counter = 0
# for li in items:
#     time = li.find_element(By.TAG_NAME, "time").text
#     event = li.find_element(By.TAG_NAME, "a").text

#     event_list[counter] = {
#             "time": time,
#             "name": event
#         }
#     counter += 1

# print(event_list)

# Alternate way

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for n in range(len(event_time)):
    event_list[n]={
        'time':event_time[n].text,
        'name':event_name[n].text,
    }
print(event_list)
# driver.quit()