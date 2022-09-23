import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POM_Service.Pages.Login_with_Gmail.login_gmail import login_using_gmail
import undetected_chromedriver as uc
import pytest

def click(driver,locator):
    WebDriverWait(driver,20).until(EC.element_to_be_clickable(locator)).click()

def submit(driver,locator):
    WebDriverWait(driver,20).until(EC.element_to_be_clickable(locator)).submit()

def Send_Keys(driver, locator,value):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable(locator)).send_keys(value)

def try_except(driver, locator):
    try:
        locator.click()
    except ElementClickInterceptedException:
        pass

class Testsample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=ser)
        driver = uc.Chrome(use_subprocess=True)
        driver.get("https://connectonetestservices.bkinfo.in/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        yield
        driver.close()
        driver.quit()

    def test_askquery(self,test_setup):
        login = login_using_gmail(driver)
        login.click_on_login()
        login.login_with_gmail()
        driver.switch_to.window(driver.window_handles[1])
        login.write_username()
        login.click_username()
        login.write_password()
        login.click_password()
        time.sleep(4)
        driver.refresh()
        driver.switch_to.window(driver.window_handles[0])
        element = driver.find_element(By.XPATH,"//*[@id='EventsListingCardView_Main_DXCardLayout0_0']/table/tbody/tr/td[2]//button[2]")
        time.sleep(4)
        ActionChains(driver).move_to_element(element).perform()
        try_except(driver,element)
        time.sleep(4)
        Send_Keys(driver, (By.ID, "textaskQuery"), "Nice event")
        driver.find_element(By.XPATH,"//input[@id='txtaskQueryPhone']").clear()
        driver.find_element(By.XPATH,"//input[@id='txtaskQueryPhone']").send_keys("8920829765")
        click(driver,(By.XPATH, "//*[@id='Query_DirectBrowse_Form']/div[3]/button[2]"))
        time.sleep(10)
        driver.find_element(By.XPATH,"//*[@id='filluserProfilePrompt']/div/div/div[2]/div/div/div/button[1]").click()

    if __name__=='__main__':
        pytest.main()

