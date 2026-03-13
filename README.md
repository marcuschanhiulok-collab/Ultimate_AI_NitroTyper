# Ultimate_AI_NitroTyper
Please help. Does not work. Supposed to work on chrome
Please look at what displays the race text
view-source:https://www.nitrotype.com/race
Code:
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
    print("Marcus: Log in and start a race.")
    input("Press ENTER when you see the 3... 2... 1... countdown!")

    words = []
    start_time = time.time()
    
    # 1. SCAN THE WHOLE PAGE: Look for the longest string of text
    while time.time() - start_time < 8: # Search for 8 seconds
        try:
            # Get all text from all 'span' tags (how Nitro Type often splits words)
            spans = driver.find_elements(By.TAG_NAME, "span")
            text_segments = [s.text.strip() for s in spans if len(s.text.strip()) > 1]
            
            # If we find enough words, we've likely found the race
            if len(text_segments) > 10:
                words = text_segments
                break
        except:
            time.sleep(0.2)

    if not words:
        print("ERROR: Still can't see the text. Try running the script after the race actually begins.")
        return

    print(f"SUCCESS! Captured {len(words)} segments. Typing...")

    # 2. TYPE INTO THE ACTIVE ELEMENT
    driver.find_element(By.TAG_NAME, "body").click()
    for word in words:
        for char in word:
            driver.switch_to.active_element.send_keys(char)
            time.sleep(random.uniform(0.12, 0.18))
        driver.switch_to.active_element.send_keys(Keys.SPACE)
        time.sleep(random.uniform(0.1, 0.2))

if __name__ == "__main__":
    start_marcus_bot()
