from environmental_setup import environmental_setup
from Locators.Home_page_locator import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class Home_Page_Methods(environmental_setup):

    def test_1_check_spring_logo(self):
        driver = self.driver
        logo_spring = driver.find_element_by_xpath(spring_stamp)
        if logo_spring.is_displayed():
            print("Logo is displaying")
        else:
            raise AssertionError("Spring Log is not displaying")

    def test_2_check_welcome_text(self):
        driver = self.driver
        text_welcome = driver.find_element_by_xpath(welcome_text)
        if text_welcome.is_displayed():
            print("Welcome Text is displaying")
        else:
            raise AssertionError("Welcome Text is not displaying")

    def test_3_check_spring_stamp(self):
        driver = self.driver
        stamp_spring = driver.find_element_by_xpath(spring_stamp)
        if stamp_spring.is_displayed():
            print("Spring Stamp is displaying at Bottom")
        else:
            raise AssertionError("Spring Stamp is not displaying at Bottom")

if __name__ == "__main__":
    unittest.main()
