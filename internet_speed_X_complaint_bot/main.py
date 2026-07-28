from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'ani98cho'
TWITTER_PASSWORD = 'Password789#'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

