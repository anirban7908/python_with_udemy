from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome open after programme finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#open chrome browser
driver = webdriver.Chrome(options=chrome_options)

# ================================ Amazom product search ===============================================
# driver.get("https://www.amazon.in/STUDDS-Helios-Asphalt-Certified-Helmet/dp/B0FC675LDR/ref=sr_1_3_sspa?dib=eyJ2IjoiMSJ9.O8c_FaJt4nrx__qWyjuortTA_s9AtNDd31vw2L8xzYX1tU9WJOgm6GxXJuVAf3aipJKW-Kw3xlPyOf6kkyXtgRHYaToB2QKo26uokvCyeOiG_0OPwBBiWwn0xblzTAhF6sD9D2T2HPJ7ND2hyOqoS-qoFo9V8MY5mX8gK_h_84PRhDvF58J6lhkeKdm6GGTis06Ry1cKUYpA3d71RfTFDTB1wG0aZLnKRuaBbWcjROr_2XOQbRnoeZJlQoIK-f1c2Km-o4rNRWedvG19uM1SfGALB_u5dd5XDM0kOwWgFmk.hYiahRMxAgWASAGHq-K8yJPsjku8o9dh7LGDrvEDNP4&dib_tag=se&keywords=full+face+helmet&pf_rd_i=5258045031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=merchandised-search-5&qid=1784619337&s=automotive&sr=1-3-spons&aref=abnVjnFu2g&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price.text)
# ================================ Amazom product search ===============================================
driver.get("https://www.python.org/")

# Find element by name
# search_bar = driver.find_element(By.NAME, value="q")
# get attribute name in a html tag
# print(search_bar.get_attribute("placeholder"))

# Find element by id
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# Find element by CSS selector
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)


# Find element by XPATH

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

print(bug_link.text)
print(bug_link.get_attribute("href"))

driver.quit()