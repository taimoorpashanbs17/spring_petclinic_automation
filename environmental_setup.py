import platform
import os
import unittest
from selenium import webdriver
import datetime


class environmental_setup(unittest.TestCase):
    def setUp(self):
        os_name = platform.system()
        current_path = os.getcwd()
        parent_directory = os.path.dirname(current_path)
        global selected_driver
        selected_browser = input("Which Browser You want to use for Testing , Press 1 for Chrome and 2 Firefox: ")
        if (os_name == 'Darwin') and (selected_browser =="1"):
            selected_driver = os.path.abspath(parent_directory+"/Drivers/Chromedriver/chromedriver_mac")
        elif (os_name == 'Darwin') and (selected_browser =="2"):
            selected_driver = os.path.abspath(parent_directory+"/Drivers/geckodriver/geckodriver_mac")
        elif (os_name == 'Linux') and (selected_browser =="1"):
            selected_driver = os.path.abspath(parent_directory+"/Drivers/Chromedriver/chromedriver_linux")
        elif (os_name == 'Linux') and (selected_browser =="2"):
            selected_driver = os.path.abspath(parent_directory+"/Drivers/geckdriver/geckodriver_linux")
        else:
            raise AssertionError("No Driver is there")

        if selected_browser == "1":
           self.driver = webdriver.Chrome(executable_path= selected_driver)
        elif selected_browser == "2":
            self.driver = webdriver.Firefox(executable_path=selected_driver)
        else:
            raise AssertionError("There is no Browser Defined")
        print("Connection has been started on " + str(datetime.datetime.now()))
        if selected_browser == "1":
            print("Environment has been Setup at Chrome Browser.")
        elif selected_browser == "2":
            print("Environment has been Setup at Firefox Browser.")
        else:
            print("There is no Browser Defined")
        self.driver.maximize_window()
        # self.driver.get("http://localhost:8080/")

    def tearDown(self):
        if (self.driver != None):
            print("--------------------------------------")
            print("Test Environment is Destroyed")
            print("Run Completed at " + str(datetime.datetime.now()))
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()

