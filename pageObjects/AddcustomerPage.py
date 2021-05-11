import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = (By.XPATH,"//a[@href='#']//span[contains(text(),'Customers')]")
    lnkCustomers_menuitem_xpath = (By.XPATH, "//span[@class='menu-item-title'][contains(text(),'Customers')]")
    btnAddnew_xpath = (By.XPATH, "//a[@class='btn bg-blue']")
    txtEmail_xpath = (By.XPATH, "//input[@id='Email']")
    txtPassword_xpath = (By.XPATH, "//input[@id='Password']")
    txtcustomerRoles_xpath = (By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']")
    lstitemAdministrators_xpath = (By.XPATH, "//li[contains(text(),'Administrators')]")
    lstitemRegistered_xpath = (By.XPATH, "//li[contains(text(),'Registered')]")
    lstitemGuests_xpath = (By.XPATH, "//li[contains(text(),'Guests')]")
    lstitemVendors_xpath = (By.XPATH, "//li[contains(text(),'Vendors')]")
    drpmgrOfVendor_xpath = (By.XPATH, "//*[@id='VendorId']")
    rdMaleGender_id = (By.ID, "Gender_Male")
    rdFeMaleGender_id = (By.ID, "Gender_Female")
    txtFirstName_xpath = (By.XPATH, "//input[@id='FirstName']")
    txtLastName_xpath = (By.XPATH, "//input[@id='LastName']")
    txtDob_xpath = (By.XPATH, "//input[@id='DateOfBirth']")
    txtCompanyName_xpath = (By.XPATH, "//input[@id='Company']")
    txtAdminContent_xpath = (By.XPATH, "//textarea[@id='AdminComment']")
    btnSave_xpath = (By.XPATH, "//button[@name='save']")

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(*self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(*self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(*self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(*self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(*self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(*self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(*self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(*self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(*"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(*self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(*self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(*self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(*self.lstitemGuests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(*self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(*self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(*self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(*self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(*self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(*self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(*self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(*self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(*self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(*self.btnSave_xpath).click()
