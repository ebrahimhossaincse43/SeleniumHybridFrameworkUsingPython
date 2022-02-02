import time

from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.LoginPage import Login
from Utilities import ExcelUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/Test_Login.xlsx"
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("***************Test_002_DDT_Login*****************")
        self.logger.info("***************Verifying Login Test***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Shhet1')
        print("Number of Rows in a Excel", self.rows)

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
