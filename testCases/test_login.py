import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities import ScreenShot
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.logGen()

    def test_homePageTitle(self, setup):
        self.logger.info("******** Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("******** Home Page Title test is passed ********")
            self.driver.close()

        else:
            ScreenShot.takeScreenshot(self.driver, 'test_homePageTitle')
            self.logger.error("******** Home Page Title test is failed ********")
            self.driver.close()

            assert False

    def test_login(self, setup):
        self.logger.info("******** Verifying Login Test ********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginpage = LoginPage(self.driver)
        self.loginpage.setUserName(self.username)
        self.loginpage.setPassword(self.password)
        self.loginpage.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("******** Login test is passed ********")
            self.driver.close()

            assert True
        else:
            ScreenShot.takeScreenshot(self.driver, 'test_login')
            self.logger.error("******** Login test is failed ********")
            self.driver.close()

            assert False
