from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://practice.automationtesting.in/my-account/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("varniktech@gmail.com", "varnik20@123")