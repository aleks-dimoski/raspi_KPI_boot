# Raspberry Pi - KPI Bootloader
Python script to access Key Performance Indicators (KPIs) on Dynamics 365 Business Central. Usage requires that the user already be logged into the Business Central environment.

## Login Setup
In order to access the Business Central environment, the user must provide a correct URL address for their company in the format of:
'''
https://businesscentral.dynamics.com/<Company Name Here>
'''
In addition, the user must log in to their company the first time that they use the script. This will be added to a new folder, raspi_KPI_boot/raspi_KPI_boot/UserData which will store all cookie information during use.

There will be a **setup.py** script (TODO) which can be run for the first execution that will generate the required files. These will include a .json file for the URL address and the UserData directory.
