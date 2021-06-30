import time
from selenium.webdriver import *
from selenium.webdriver.common.keys import Keys


def access_power_bi(driver):
    """Accepts webdriver as input. Expands PowerBI display, then enables fullscreen."""

    # Maximize window.
    driver.fullscreen_window()
    time.sleep(40)

    # Drop down list of options for PowerBI Reports.
    try:
        drop_down = driver.find_element_by_xpath(".//*[@title='Actions for Power BI Reports']")
        drop_down.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        print("Drop down selection failed. Attempted to access and click 'Actions for Power BI Reports'. Ensure that the correct URL is being accessed.")

    # Click on 'Expand Report' option.
    try:
        expand_report = driver.find_element_by_xpath(".//li[@title='View all information in the report.']")
        expand_report.click()
        time.sleep(5)
    except Exception as e:
        print(e)
        print("Expand report failed. Attempted to access and click 'View all information in the report.'. Ensure that the website is correct and possesses this element")

    # Wait (TODO)
    time.sleep(600)
