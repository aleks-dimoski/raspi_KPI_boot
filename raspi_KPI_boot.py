import os
from raspi_KPI_boot.net import *
from raspi_KPI_boot.business_central import *

print("Beginning process...")

driver = open_browser()
access_power_bi(driver)

print("Process complete. Closing.")
driver.close()
