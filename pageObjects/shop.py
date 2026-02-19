from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.common.by import By

from utils.util import Util
class ShoppingPage(Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.addToCartBtns = (By.CSS_SELECTOR,"button[class='btn btn-info']")
        self.checkOut = (By.PARTIAL_LINK_TEXT,"Checkout")
        self.checkOut2 = (By.XPATH,"//button[contains(text(),'Checkout')]")
        self.driver = driver
    def shopping(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_all_elements_located(self.addToCartBtns))
        list = self.driver.find_elements(*self.addToCartBtns)
        for i in list:
            i.click()
        self.driver.find_element(*self.checkOut).click()
        self.driver.find_element(*self.checkOut2).click()
    