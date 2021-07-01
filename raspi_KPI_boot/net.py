#!/usr/bin/env python

import time
from selenium.webdriver import *
from selenium.webdriver.chrome.options import Options


def open_browser():
    options = Options()
    options.add_argument("--user-data-dir=/home/pi/Documents/raspi_KPI_boot/raspi_KPI_boot/UserData")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.page_load_strategy = 'normal'
    chrome = Chrome(options=options)
    time.sleep(5)
    chrome.fullscreen_window()
    chrome.get("https://app.powerbi.com/reportEmbed?reportId=5704703e-aa64-4a74-bc30-1237cabd070a&autoAuth=true&ctid=b81d529b-fe2b-4e03-a276-8e8ae55f9c58&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLXdlc3QtZXVyb3BlLWItcHJpbWFyeS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldC8ifQ%3D%3D")
    time.sleep(5)
    return chrome


def get_user_details():
    file = open("DATA.json", "r")
    file.close()
