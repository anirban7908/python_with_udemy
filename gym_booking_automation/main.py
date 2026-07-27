import os
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------
# Credentials
USER_NAME = "anirban_test@test.com"
PASSWORD = "AnirbanGymPass123"
GYM_URL = "https://appbrewery.github.io/gym/"

# Chrome Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Make dir to store chrome profiles
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# Driver setup
driver = webdriver.Chrome(chrome_options)
driver.get(GYM_URL)


# ----------------  Step 2 - Automated Login ----------------
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)


def login():
    # Setting wait time to reload the page properly
    wait = WebDriverWait(driver, 5)

    try:
        # Wait until the login element appears and click it once appears
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
    except NoSuchElementException as nse:
        print(f"Element Not found: {nse}")
    except ElementNotInteractableException as ni:
        print(f"Element is Not Interactable: {ni}")

    try:
        # Wait until the form elements appears and click them once appears
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(USER_NAME)

        password_input = wait.until(
            EC.element_to_be_clickable((By.ID, "password-input"))
        )
        password_input.clear()
        password_input.send_keys(PASSWORD)

        submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
        submit_button.click()
    except NoSuchElementException as nse:
        print(f"Element Not found: {nse}")

    # Wait until for the schedule page to load.
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))


retry(login, description="Login")
# ----------------  Step 3 - Class Booking: Book Upcoming Tuesday Class  ----------------


def book_class():

    # Find all class cards
    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    # Counters for booked classes for the booking summary
    booked_count = 0
    waitlist_count = 0
    already_booked_count = 0
    processed_class = []
    for card in class_cards:
        # Get the day title from the parent day group
        day_group = card.find_element(
            By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]"
        )
        day_title = day_group.find_element(By.TAG_NAME, "h2").text

        # Check if this is a Tuesday
        if "Tue" in day_title or "Thu" in day_title:
            # Check if this is a 6pm class
            time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00 PM" in time_text:
                # Get the class name
                class_name = card.find_element(
                    By.CSS_SELECTOR, "h3[id^='class-name-']"
                ).text

                # Find and click the book button
                button = card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']"
                )
                button_text = card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']"
                ).text

                class_info = f"{class_name} on {day_title}"

                # Increment the counter(s)
                if button.text == "Booked":
                    print(f"✓ Already booked: {class_info}")
                    already_booked_count += 1
                    processed_class.append(f"[Already Booked]: {class_info}")
                elif button.text == "Waitlisted":
                    print(f"✓ Already on waitlist: {class_info}")
                    already_booked_count += 1
                    processed_class.append(f"[Already Waitlist]: {class_info}")
                elif button.text == "Book Class":
                    button.click()
                    print(f"✓ Successfully booked: {class_info}")
                    booked_count += 1
                    # Wait a moment for the button state to update
                    time.sleep(0.5)
                    processed_class.append(f"[New Booked]: {class_info}")
                elif button.text == "Join Waitlist":
                    button.click()
                    print(f"✓ Joined waitlist for: {class_info}")
                    waitlist_count += 1
                    # Wait a moment for the button state to update
                    time.sleep(0.5)
                    processed_class.append(f"[New Waitlist]: {class_info}")


    # Print summary
    print("\n--- BOOKING SUMMARY ---")
    print(f"Classes booked: {booked_count}")
    print(f"Waitlists joined: {waitlist_count}")
    print(f"Already booked/waitlisted: {already_booked_count}")
    print(
        f"Total Tuesday & Thursday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}"
    )

    print("\n--- DETAILED CLASS LIST ---")
    for class_detail in processed_class:
        print(f"  • {class_detail}")


def get_my_bookings():
    booking_page = driver.find_element(By.ID, "my-bookings-link")
    booking_page.click()


book_class()
time.sleep(2)
get_my_bookings()