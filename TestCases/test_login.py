import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    # def test_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp = Login(self.driver)
    #     self.lp.setUserName(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     time.sleep(2)
    #     act_title = self.driver.title
    #     print(act_title)
    #     self.driver.close()
    #
    #     if act_title == "Dashboard / nopCommerce administratio":
    #         assert True
    #         self.driver.close()
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
    #         self.driver.close()
    #         assert False
