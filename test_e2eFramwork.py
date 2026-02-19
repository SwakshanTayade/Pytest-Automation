import json
import pytest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support import expected_conditions
from pageObjects.login import LoginPage
from pageObjects.shop import ShoppingPage
from pageObjects.checkout import CheckoutPage
import time

data_file_path = "./data/test_e2eFramwork.json"

with open(data_file_path,'r') as reader:
    res = json.load(reader)
    data = res["data"]
    print("The data is:",data)
@pytest.mark.usefixtures("browserInvoke")
@pytest.mark.parametrize("test_data_item",data)
class TestFramework:
    def test_e2eframework(self,browserInvoke, test_data_item):
        global driver
        driver = browserInvoke
        # driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/loginpagePractise/")

        loginPage = LoginPage(driver)
        loginPage.login(test_data_item["username"],test_data_item["password"])
        print(loginPage.getTitle())
        shopPage = ShoppingPage(driver)
        shopPage.shopping()
        print(shopPage.getTitle())
        checkoutPage = CheckoutPage(driver)
        checkoutPage.checkout(test_data_item["country"],test_data_item["expectedCountry"])
        print(checkoutPage.getTitle())

