from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME = (By.ID, "Email")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BTN = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(*self.USERNAME).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def clickLogout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()