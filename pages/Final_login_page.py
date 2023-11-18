import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _email_field = "username"
    _password_field = "password"
    _login_button = "login"


    def enterEmail(self, email):
        self.sendkeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendkeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def login(self, email, password):
        #self.clickMyAccountink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//a[text()='Logout']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("/html/body/div[1]/div[2]/div/div/div/div/div[1]/ul/li/text()[1]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Account - Automation Practice Site")
