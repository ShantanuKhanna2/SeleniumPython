import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POM_Service.Pages.Login_with_Gmail.login_gmail import login_using_gmail
import undetected_chromedriver as uc
import pytest

def click(driver,locator):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable(locator)).click()

def Send_Keys(driver, locator,value):
    WebDriverWait(driver,10).until(EC.visibility_of(locator)).send_keys(value)

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
        driver.find_element(By.XPATH,"//*[@id='EventsListingCardView_Main_DXCardLayout0_0']/table/tbody/tr/td[2]//button[2]").click()
        login = login_using_gmail(driver)
        login.login_with_gmail()
        driver.switch_to.window(driver.window_handles[1])
        login.write_username()
        login.click_username()
        login.write_password()
        login.click_password()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.ID,"textaskQuery").send_keys("Nice event")
        time.sleep(4)
        Send_Keys(driver,(By.XPATH,"//input[@id='txtaskQueryPhone']"),"8934567890")
        driver.find_element(By.XPATH, "//*[@id='Query_DirectBrowse_Form']/div[3]/button[2]").click()
        time.sleep(4)
        

