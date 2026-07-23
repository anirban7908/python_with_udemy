from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

driver.get('https://ozh.github.io/cookieclicker/')

sleep(2)



print("Searching for the Cookie element!")

try:
    language = driver.find_element(By.ID, "langSelect-EN")
    language.click()
    sleep(3)
    
except NoSuchElementException:
    print('Cookie element not found!')
    

sleep(2)
cookie = driver.find_element(By.ID, 'bigCookie')

all_products = [f"product{i}" for i in range(20)]


wait_time = 5
timeout = time()+wait_time
five_min = time() + 60 * 5


while True:
    cookie.click()

    if time()>timeout:
        try:
            cookies_elem = driver.find_element(By.ID, 'cookies')
            cookie_text = cookies_elem.text
            cookie_count =  cookie_text.split()[0].replace(",","")
            
            # Getting all the products
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
        
            timeout = time() + wait_time
            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products):  # Start from most expensive (bottom of list)
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # Stop after 5 minutes
    if time() > five_min:
        try:
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break