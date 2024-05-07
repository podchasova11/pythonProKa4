import time

from  selenium import webdriver
from selenium.webdriver.options import Options

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=XSDTRCYFGUVJYBHIKULNM")
driver = webdriver.Chrome(options=options)


