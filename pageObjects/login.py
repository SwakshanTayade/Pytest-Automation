from selenium.webdriver.common.by import By
import time

from utils.util import Util
class LoginPage(Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.username_input = (By.ID,"username")
        self.password_input = (By.ID,"password")
        self.terms = (By.ID,"terms")
        self.signInBtn = (By.ID,"signInBtn")
        self.driver = driver
    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.signInBtn).click()