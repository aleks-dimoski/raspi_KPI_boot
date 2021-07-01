#!/usr/bin/env python

import time
from selenium.webdriver import *
from selenium.webdriver.common.keys import Keys


def access_power_bi(driver):
    """Accepts webdriver as input. Expands PowerBI display, then enables fullscreen."""

    # Clicks on sign-in button (must already be signed into PowerBI in cookie history).
    sign_in = driver.find_elements_by_xpath("//*[@class='bibutton primary']")
    print(sign_in[0])
    sign_in[0].click()

    # Wait and maximize screen (TODO)
    time.sleep(20)
    driver.fullscreen_window()
    time.sleep(28800)
