from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

DUMMY_TINDER_URL = 'https://app.100daysofpython.dev/services/tindog/u/tLa1NP5oSz-6ce4niHC97ZFMOetbMcDl'
FACEBARK_EMAIL = "anirban.choudhury.7908@gmail.com"
FACEBARK_PASSWORD = "Password789#"
# ==========Chrome setup===========
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# =============Create Driver and open Tinder dummy===============
driver = webdriver.Chrome(chrome_options)
driver.get(DUMMY_TINDER_URL)

# ================Find for the login button and login into the website=============
wait = WebDriverWait(driver, 5)
try:
    login_button = wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body/header/button")))
    login_button.click()
    
    face_bark_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="login-modal"]/div/div/div/button[1]')))
    face_bark_button.click()

    # ========================Driver Window Handlers====================
    all_window_handles = driver.window_handles
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    
    # ----Change to current window from the base window-----
    
    driver.switch_to.window(fb_login_window)

    # Facebark Form Fillup
    email = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    email.clear()
    email.send_keys(FACEBARK_EMAIL)
    
    password = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="pass"]')))
    password.clear()
    password.send_keys(FACEBARK_PASSWORD)
    
    submit_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/form/button')))
    submit_btn.click()
    
    # ----Returning back to the current window and hit the popup button-------
    driver.switch_to.window(base_window)
    
    popup_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button')))
    popup_btn.click()
    
    # Hitting the no thanks button
    Not_interested_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button[2]')))
    Not_interested_btn.click()
    
    # Hitting the accept cookie button
    Cookie_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/form/button')))
    Cookie_btn.click()
    
    # =======Entering the tindog app===========
    for i in range(20):
        like_btn = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="like-button-container"]/form/button'))) 
        like_btn.send_keys(Keys.ENTER) 
        time.sleep(3)  
except NoSuchElementException as nse:
    print(f"Element Not found: {nse}")
    
