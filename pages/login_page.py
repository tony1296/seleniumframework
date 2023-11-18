from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _email_field = "username"
    _password_field = "password"
    _login_button = "login"

    #page method for email of login page
    def enterEmail(self, email):
        self.sendkeys(email, self._email_field)
    #page method fo password of login page
    def enterPassword(self, password):
        self.sendkeys(password, self._password_field)
    #page method for login button
    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")
    #login method for login page

    def login(self, email, password):

        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

