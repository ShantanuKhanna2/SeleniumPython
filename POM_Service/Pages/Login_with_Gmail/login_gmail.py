from selenium.webdriver.common.by import By

class login_using_gmail():

    def __init__(self, driver):
        self.driver = driver
        self.click_on_login_id = "loginbtn_atag"
        self.login_with_gmail_xpath = "//*[@id='loginmdl']/div/div/div/div[2]/a/b"
        self.choose_username_id = "identifierId"
        self.click_username_xpath = "//*[@id='identifierNext']/div/button/span"
        self.choose_password_name = "password"
        self.click_password_xpath = "//*[@id='passwordNext']/div/button/span"

    def click_on_login(self):
        self.driver.find_element(By.ID,self.click_on_login_id).click()

    def login_with_gmail(self):
        self.driver.find_element(By.XPATH,self.login_with_gmail_xpath).click()

    def write_username(self):
        self.driver.find_element(By.ID,self.choose_username_id).send_keys("shantanukhanna2@gmail.com")

    def click_username(self):
        self.driver.find_element(By.XPATH,self.click_username_xpath).click()

    def write_password(self):
        self.driver.find_element(By.NAME,self.choose_password_name).send_keys("SK8527264564")

    def click_password(self):
        self.driver.find_element(By.XPATH,self.click_password_xpath).click()










