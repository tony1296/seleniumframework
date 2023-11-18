"""
@package base
Webdriver factory class implementation
It creates a web driver instance based on browser configuration
Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None

        """
        self.browser = browser


    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

         Returns:
              'WebDriver Instance'
        """
        baseURL = "http://practice.automationtesting.in"
        if self.browser == "edge":
            driver = webdriver.Edge()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(3)

        driver.maximize_window()
        driver.get(baseURL)
        return driver
