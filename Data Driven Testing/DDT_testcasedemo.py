import time

import Xlutils
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
driver = webdriver.Chrome(service=ser)

def is_element_present(how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except NoSuchElementException:
        return False

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(1)

path = "../Data Driven Testing/DDT_testdata_sample.xlsx"
row = Xlutils.getRowCount(path,"sheet1")
column = Xlutils.getColumnCount(path,"sheet1")


for r in range(2,row+1):
    username = Xlutils.readData(path,"sheet1",r,1)
    password = Xlutils.readData(path,"sheet1",r,2)

    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

    if is_element_present(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[1]/a/div[1]"):
        print("Test passed")
        Xlutils.writeData(path,"sheet1",r,3,"test passed")
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img").click()
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

    else:
        print("Test Failed")
        Xlutils.writeData(path,"sheet1",r,3,"test failed")
        driver.refresh()

driver.quit()

