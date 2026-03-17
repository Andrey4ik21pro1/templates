from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import re
import time

def main():
    url = "https://www.google.com"

    options = Options()
    options.add_argument("--disable-backgrounding-occluded-windows")
    options.add_argument("--disable-background-timer-throttling")
    options.add_argument("--disable-renderer-backgrounding")
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    try:
        driver.get(url)
        input("Press Enter to continue...")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()