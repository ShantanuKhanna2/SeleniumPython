import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest


# def assertEqual(param, title):
#     pass


class TestSamplepaper():
    @pytest.fixture()
    def test_setup(self):
        global driver
        ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get("https://connectonetestservices.bkinfo.in/")
        titleofWebpage= self.driver.title
        yield
        self.driver.close()
        self.driver.quit()

    def test_page_title(self, test_setup):
        self.driver.get("https://www.google.com/")
        assert "Googles" in self.driver.title


