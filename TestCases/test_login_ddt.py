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

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel", self.rows)

        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            print(act_title)
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************Login Test is passed***************")
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***************Login Test is Failed***************")
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("***************Login Test is Failed***************")
                    lst_status.append("Failed")
                elif self.exp == "Fail":
                    self.logger.info("***************Login Test is Passed***************")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT test passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT test failed ****")
            self.driver.close()
            assert False

        self.logger.info("******** End of Login DDT Test ********")
        self.logger.info("**************** Completed TC_LoginDDT_e02 ************")
