import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=XSDTRCYFGUVJYBHIKULNM")
driver = webdriver.Chrome(options=options)


driver.get("https://hyperskill.org/tracks")
FOR_BUSINES_BUTTON_LOCATOR = (("xpath"), "//a[text()=' For Business '])[1]]")
START_FOR_FREE_BUTTON_LOCATOR = (("xpath"), "//a[text()='Start for Free'])[1]]")
driver.find_element(*FOR_BUSINES_BUTTON_LOCATOR).click()
time.sleep(3)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.find_element(*START_FOR_FREE_BUTTON_LOCATOR).click()
time.sleep(3)

