import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.select import Select
import pytest

class Testsample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
        driver = webdriver.Chrome(service=ser)
        driver.get("https://connectonetestservices.bkinfo.in/")
        yield
        driver.close()
        driver.quit()

    def test_filter(self, test_setup):
        filter = driver.find_element(By.ID, "FilterButton")
        ActionChains(driver).move_to_element(filter).perform()
        driver.find_element(By.ID, "GLookUp_State").click()
        driver.find_element(By.XPATH,"//*[@id='LookUp_GetStatesList_El_datagrid']/div/div[6]/div/div/div[1]/div/table/tbody/tr[6]/td").click()
        driver.find_element(By.XPATH,"//input[@id='SpeakerName']").send_keys("abc")
        driver.find_element(By.XPATH, "//*[@id='filtermenu']/div/a[2]").click()

    def test_givefeedback(self, test_setup):
        driver.find_element(By.XPATH,"//*[@id='EventsListingCardView_Main_DXCardLayout0_0']/table/tbody/tr/td[2]/div/div/div/div[1]/div/div[2]/button[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//*[@id='feedbackprompt']/div/div/div[3]/button[2]").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//*[@id='feedbackratingcntl']/a[3]").click()
        driver.find_element(By.ID,"textareaFeedbackText").send_keys("Good job")
        driver.find_element(By.ID,"btnFeedbackSubmit").click()
