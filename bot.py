from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
def start_marcus_bot():
    driver.get("https://www.nitrotype.com")
    print("Marcus: Log in and join a race.")
    input("Press ENTER when you see the 3... 2... 1... countdown!")
    # 1. THE POWER SEARCH: Keep looking for 10 seconds
    words = []
    print("Searching for race text... (Keep the Chrome window visible!)")
    start_search = time.time()
    while time.time() - start_search < 10: # Look for 10 seconds
        try:
            # Nitro Type often uses 'dash-copy' for the whole block
            container = driver.find_element(By.CLASS_NAME, "dash-copy")
            if container.text and len(container.text) > 10:
                words = container.text.split()
                break
        except:
            time.sleep(0.1) # Check again very quickly
    if not words:
        print("STILL NO TEXT! Marcus, check if the words are inside a different box.")
        return
    print(f"SUCCESS! Found {len(words)} words. Typing now...")
    # 2. TYPE INTO THE ACTIVE ELEMENT
    # We click the body first to make sure the keyboard is 'focused'
    driver.find_element(By.TAG_NAME, "body").click()
    for word in words:
        for char in word:
            driver.switch_to.active_element.send_keys(char)
            time.sleep(random.uniform(0.12, 0.19)) # ~70 WPM
        driver.switch_to.active_element.send_keys(Keys.SPACE)
        time.sleep(random.uniform(0.08, 0.15))
if __name__ == "__main__":
    start_marcus_bot()
