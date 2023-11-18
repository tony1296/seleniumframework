from pages.Final_login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetUp):
        self.lp = LoginPage(self.driver)

        self.ts = TestStatus(self.driver)



    @pytest.mark.run(order=1)
    def test_validLogin(self):
        baseURL = "https://practice.automationtesting.in/my-account/"


        self.lp.login("varniktech@gmail.com", "varnik20@123")
        result1 = self.lp.verifyLoginTitle()
        print(result1)
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        assert result2 == True
        self.ts.markFinal("test_validLogin", result2, "Login Verification")
        self.ts.mark("test_validLogin", result2, "Login Verification")
        self.driver.quit()

    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        self.lp.login("varniktech@gmail.com", "varnik20@12")
        result = self.lp.verifyLoginFailed()
        assert result == False
