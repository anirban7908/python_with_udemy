import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotInteractableException,
    ElementNotSelectableException,
    TimeoutException
)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
from time import sleep

load_dotenv()

URL=os.getenv('INSTAGRAM_URL')
EMAIL=os.getenv('EMAIL')
PASSWORD=os.getenv('PASSWORD')
SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

class InstagramBot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(chrome_options)
        self.default_wait = WebDriverWait(self.driver, 3)
    
    def login(self, email, password, url):
        max_retries = 3
        current_try = 0
        
        if not (email and password and url):
            print("Email or Password or Site url is missing!")
            return False 
        
        #calling the url
        self.driver.get(url)
        
        while current_try < max_retries:
            try:
                if current_try == 0:
                    # Checking the email and password inputs
                    email_input = self.default_wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div/aside/div/form/input[1]')))
                    password_input = self.default_wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/div/aside/div/form/input[2]')))
                else:
                    email_input = self.default_wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="username"]')))
                    password_input = self.default_wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="password"]')))
                
                email_input.clear()
                email_input.send_keys(EMAIL)
                password_input.clear()
                password_input.send_keys(PASSWORD, Keys.ENTER) 
            except TimeoutException:
                print("Could not find the login input fields!")
                return False

            try:
                home_button = self.default_wait.until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[1]/nav/a[2]/span'))).text
                if home_button == 'Home':
                    print("Login Successful")
                
                    try:
                        not_now_button_user_info = self.default_wait.until(ec.element_to_be_clickable((
                            By.XPATH, "//div[contains(@class, 'naan-popup-card')]//div[text()='Not now']"
                        )))
                        not_now_button_user_info.click()
                        
                        not_now_button_notification = self.default_wait.until(ec.element_to_be_clickable((
                            By.XPATH, "//div[contains(@class, 'naan-popup-card')]//button[text()='Not Now']"
                        )))
                        not_now_button_notification.click()
                    except TimeoutException:
                        print("Pop-ups did not appear, proceeding anyway.")
                    
                    return True
            except TimeoutException:
                current_try += 1
                print(f"Login failed. Attempt {current_try} of {max_retries}.")
                
                try:
                    # Capture and print the on-screen error banner message if present
                    error_div_text = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]").text
                    print(f"Error Banner Text: {error_div_text}")
                except:
                    print("No visible error banner text found on screen.")
                    
                sleep(2)  
        
        print("Maximum retries reached. Login failed completely.")
        return False
      
                
    def find_followers(self, similar_account):
        # 1. Click the Search button in the navigation panel
        try:
            # Look for a nav button containing search context or fallback to your path
            search_btn = self.default_wait.until(
                ec.element_to_be_clickable((By.XPATH, "//nav//button[contains(., 'Search')] | /html/body/div[1]/nav/button"))
            )
            search_btn.click()
        except TimeoutException:
            print("Search button not found in navigation!")
            return False

        # 2. Find the input box and type the target account name
        try:
            search_bar = self.default_wait.until(
                ec.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search'] | /html/body/aside/div[2]/input"))
            )
            search_bar.clear()
            search_bar.send_keys(similar_account)
            sleep(2) # Give the dropdown list a brief moment to load results
        except TimeoutException:
            print("Search bar input field failed to load!")
            return False

        # 3. CRITICAL FIX: Click the actual target account profile from the search dropdown results list
        try:
            # This looks for the first search item in the list matching your text
            first_result = self.default_wait.until(
                ec.element_to_be_clickable((By.XPATH, f"//aside//a[contains(@href, '{similar_account}')]"))
            )
            first_result.click()
        except TimeoutException:
            print(f"Account '{similar_account}' did not show up in the search results list!")
            return False

        # 4. Verify that you have successfully landed on the profile page
        try:
            # Wait for the main profile header username text element to load
            profile_header = self.default_wait.until(
                ec.visibility_of_element_located((By.XPATH, "//header//h2 | //header//h1"))
            )
            
            if similar_account.lower() in profile_header.text.lower():
                print(f"Successfully landed on {similar_account}'s profile page.")
                return True
            else:
                print(f"Header text '{profile_header.text}' doesn't match '{similar_account}'!")
                return False
                
        except TimeoutException:
            print("Landed on page, but profile details failed to load.")
            return False

    def follow(self):
        pass

bot = InstagramBot()
login_try = bot.login(EMAIL,PASSWORD,URL)
if login_try:
    find_similar_acc = bot.find_followers(SIMILAR_ACCOUNT)
    if find_similar_acc:
        