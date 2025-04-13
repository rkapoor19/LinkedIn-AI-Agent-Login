from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Credentials
EMAIL = "***"
PASSWORD = "***"

def login_linkedin():
    # Set up Chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)

    # Step 1: Go to LinkedIn
    driver.get("https://www.linkedin.com/login")

    # Step 2: Enter email
    email_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    email_input.send_keys(EMAIL)

    # Step 3: Enter password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    # Step 4: Confirm login
    try:
        wait.until(EC.presence_of_element_located((By.ID, "global-nav-search")))
        print("✅ Successfully signed in to LinkedIn.")
    except:
        print("❌ Failed to sign in. Check credentials or login issues.")

    # Optional: Keep browser open for observation
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    login_linkedin()
