import time
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options


def open_browser():
    options = Options()
    options.add_argument("--user-data-dir=/home/pi/Documents/raspi_KPI_boot/raspi_KPI_boot/UserData")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.page_load_strategy = 'normal'
    ff = Chrome(options=options)
    ff.get("https://businesscentral.dynamics.com/BoA")
    time.sleep(60)
    return ff


def get_user_details():
    file = open("DATA.json", "r")
    file.close()
