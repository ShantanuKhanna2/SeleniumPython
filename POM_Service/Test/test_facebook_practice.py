from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

#class Testdemo():
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

def test_login_facebook(test_setup):
    driver.find_element(By.ID,"email").send_keys("shantanukhanna2@gmail.com")
    driver.find_element(By.ID,"pass").send_keys("Shaan@123$")
    driver.find_element(By.NAME,"login").click()

def test_teardown():
    driver.close()
