from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options

import time


def open_browser():
    options = Options()
    options.add_argument("--user-data-dir=/home/pi/Documents/raspi_KPI_boot/raspi_KPI_boot/UserData")
    options.page_load_strategy = 'normal'
    chrome = Chrome(options=options)
    chrome.get("https://businesscentral.dynamics.com/BoA")
    time.sleep(600)
