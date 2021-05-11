import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities import ScreenShot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtil

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"

    logger = LogGen.logGen()

    def test_ddt_login(self, setup):
        self.logger.info("******** Verifying DDT Login Test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage = LoginPage(self.driver)

        self.rows = ExcelUtil.get_rowcount(self.path, 'Sheet1')
        print(self.rows)

        lst_status = []
        for r in range(2, self.rows+1):
            self.user = ExcelUtil.read_data(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtil.read_data(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtil.read_data(self.path, 'Sheet1', r, 3)

            self.loginpage.setUserName(self.user)
            self.loginpage.setPassword(self.password)
            self.loginpage.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("******** Passed ********")
                    self.loginpage.clickLogout()
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.info("******** Failed ********")
                    self.loginpage.clickLogout()
                    lst_status.append('Fail')
            elif act_title != exp_title:
                if self.exp == 'Fail':
                    self.logger.info("******** Passed ********")
                    lst_status.append('Pass')
                elif self.exp == 'Pass':
                    self.logger.info("******** Failed ********")
                    lst_status.append('Fail')

        assert 'Fail' not in lst_status
        self.logger.info("******** Login DTT Test Passes ********")
