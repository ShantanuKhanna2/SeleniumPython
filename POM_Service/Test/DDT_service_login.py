import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import Xlutils_service
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver.v2 as uc
from selenium.webdriver.support import ui

class My_Chrome(uc.Chrome):
    def __del__(self):
        pass

ser = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=ser)
driver = My_Chrome(use_subprocess=True)
driver.get('https://connectonetestservices.bkinfo.in/')
driver.maximize_window()
driver.implicitly_wait(10)

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
def is_element_present(how, what):
    try:
        driver.find_element(by=how, value=what)
        return True
    except ignored_exceptions:
        return False

def click(driver, locator):
    WebDriverWait(driver,10).until(EC.presence_of_element_located(locator)).click()

path = "DDT_service_login_gmail.xlsx"
row = Xlutils_service.getRowCount(path,"sheet1")
column = Xlutils_service.getColumnCount(path,"sheet1")

windows = driver.window_handles
for window in windows:
    print(window)
    driver.switch_to.window(window)

for r in range(2,row+1):
    username = Xlutils_service.readData(path,"sheet1",r,1)
    password = Xlutils_service.readData(path,"sheet1",r,2)

    driver.find_element(By.ID,"loginbtn_atag").click()
    click(driver,(By.XPATH,"//*[@id='loginmdl']/div/div/div/div[2]/a/b"))
    driver.refresh()
    driver.switch_to.window(driver.window_handles[1])
    if is_element_present(By.XPATH,"//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[4]/div/div/div[2]"):
        #driver.find_element(By.XPATH,"//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[4]/div/div/div[2]").click()
        driver.find_element(By.ID,"identifierId").send_keys(username)
        driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()
        driver.find_element(By.NAME,"password").send_keys(password)
        driver.find_element(By.XPATH,"//*[@id='passwordNext']/div/button/span").click()
        time.sleep(4)

    else:
        driver.find_element(By.ID, "identifierId").send_keys(username)
        driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button/span").click()
        time.sleep(4)


    if is_element_present(By.ID,"loginuseremail"):
        print("Test passed")
        Xlutils_service.writeData(path,"sheet1",r,3,"test passed")
        driver.switch_to.window(driver.window_handles[0])
        #menu = driver.find_element(By.XPATH,"//*[@id='profilelist']/a")
        # menu = ui.WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='profilelist']/a")))
        # time.sleep(4)
        # ActionChains(driver).move_to_element(menu).perform()
        # time.sleep(4)
        # driver.find_element(By.ID,"loginbtn_atag").click()
        # logout = driver.find_element(By.XPATH,"//*[@id='profilelist']/ul/li[7]/a").click()
        # time.sleep(2)

    elif is_element_present(By.ID,"loginuseremail"):
        print("Test passed")
        Xlutils_service.writeData(path,"sheet1",r,3,"test passed")
        driver.switch_to.window(driver.window_handles[0])
        #driver.find_element(By.ID, "loginbtn_atag").click()

        # menu = driver.find_element(By.XPATH,"//*[@id='profilelist']/a")
        # time.sleep(2)
        # ActionChains(driver).move_to_element(menu).perform()
        # logout = driver.find_element(By.XPATH,"//*[@id='profilelist']/ul/li[7]/a").click()
        # time.sleep(2)

    else:
        print("Test Failed")
        Xlutils_service.writeData(path,"sheet1",r,3,"test failed")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

