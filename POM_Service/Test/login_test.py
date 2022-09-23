import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))


from POM_Service.Pages.Login_with_Gmail.login_gmail import login_using_gmail


class Test_Login(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser)
        cls.driver = uc.Chrome(use_subprocess=True)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver= self.driver
        driver.get("https://connectonetestservices.bkinfo.in/")
        login = login_using_gmail(driver)
        login.click_on_login()
        login.login_with_gmail()
        driver.switch_to.window(driver.window_handles[1])
        login.write_username()
        login.click_username()
        login.write_password()
        login.click_password()
        time.sleep(4)
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element(By.XPATH,"//*[@id='loginmdl']/div/div/div/div[2]/button/span")
        time.sleep(4)
        assert 'Brahmakumaris' in driver.find_elements(By.ID,"ServiceModule_pageTitle")

    def test_page_title(self):
        self.driver.get("https://connectonetestservices.bkinfo.in/")
        assert self.driver.find_element(By.ID,"loginuseremail") == "shantanukhanna2@gmail.com"

    if __name__=='__main__':
        unittest.main()

