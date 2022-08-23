# This is a sample Python script.
#        20_8_2022
#      created by Dima
#   Automation app for rt-ed.co.il
#  start with :  pip install -r requirements.txt
# --------------------------------------------------------------------------------------
import time
from selenium import webdriver
from pom.tests import menu_test


def setUpDriver():
    dr = webdriver.Chrome('source/chromedriver.exe')
    dr.maximize_window()
    return dr


def closeDriver(dr):
    dr.close()
    dr.quit()


if __name__ == '__main__':
    driver = setUpDriver()
    menu_test.zorconnectionbtn_test(driver)
    time.sleep(3)
    driver.back()
    time.sleep(3)
    menu_test.odotbtn_test(driver)
    time.sleep(3)
    closeDriver(driver)

