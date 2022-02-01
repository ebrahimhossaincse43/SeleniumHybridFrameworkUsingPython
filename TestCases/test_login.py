import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("***************TEST_001_Login***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.logger.info("***************Verifying Home Page Title***************")
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***************Home Page Title is passed***************")
        else:
            self.driver.save_screenshot("./Screenshots/test_homePageTitle.png")
            self.driver.close()
            assert False
            self.logger.error("***************Home Page Title is failed***************")

    def test_login(self, setup):
        self.logger.info("***************Verifying Login Test***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(2)
        act_title = self.driver.title
        print(act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************Login Test is passed***************")
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/test_login.png")
            self.driver.close()
            self.logger.error("***************Login Test is passed***************")
            assert False
