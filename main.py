import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# Here Chrome  will be used
ser = Service(executable_path="C:\\Users\Shantanuk\PycharmProjects\ServiceModule\driver\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://app.shipway.com/merchant.php?dispatch=auth.login_form&return_url=merchant.php")
driver.find_element(By.ID,"username").send_keys("Shantanu.khanna1@shipway.in")
driver.find_element(By.ID,"password").send_keys("Shaan@123")
driver.find_element(By.NAME,"dispatch[auth.login]").click()
time.sleep(4)
driver.find_element(By.NAME,"order_ids[]").click()
driver.find_element(By.ID,"opener_assign_trackingnumber").click()
drop = driver.find_element(By.ID,"courier_id")
select= Select(drop)
select.select_by_visible_text("Shipway Amazon Shipping (0.5kg)")
# filter = driver.find_element(By.XPATH, "//*[@id='header_subnav']/ul/li[7]/a")
# ActionChains(driver).move_to_element(filter).perform()
# dropdown= driver.find_element(By.ID, "GLookUp_State").click()
# select = Select(dropdown)
# select.select_by_index(1)

options = driver.find_elements(By.TAG_NAME,"option")

for option in options:
    print(option.text)

print(len(options))
# # URL of website
# url = "https://connectonetestservices.bkinfo.in/#"
#
# # Opening the website
# driver.get(url)
#
# # Getting current URL source code
# get_title = driver.title
#
# # Printing the title of this URL
# print(get_title)