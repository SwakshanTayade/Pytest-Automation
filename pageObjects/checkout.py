from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from utils.util import Util
class CheckoutPage(Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.country = (By.ID,"country")
        self.countryList = (By.CSS_SELECTOR,"div.suggestions ul li")
        self.checkBox = (By.CSS_SELECTOR,"label[for='checkbox2']")
        self.submitBtn = (By.CSS_SELECTOR,"input[type = 'submit']")
        self.msg = (By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']")
    def checkout(self, country, expectedCountry):
        self.driver.find_element(*self.country).send_keys(country)
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_all_elements_located(self.countryList))
        list = self.driver.find_elements(*self.countryList)
        for i in list:
            if i.text == expectedCountry:
                print("Selected Country is (changed by develop branch): ",i.text)
                i.click()
                break
        wait.until(expected_conditions.presence_of_element_located(self.checkBox))
        self.driver.find_element(*self.checkBox).click()
        self.driver.find_element(*self.submitBtn).click()
        message = self.driver.find_element(*self.msg).text 
        print("The message: ",message)
        assert "Success" in message
