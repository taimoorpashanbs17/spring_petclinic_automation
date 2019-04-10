import platform
import os
import unittest
from selenium import webdriver
import datetime


class environmental_setup(unittest.TestCase):
    def setUp(self):
        os_name = platform.system()
        current_path = os.getcwd()
        global selected_driver
        selected_browser = input("Which Browser You want to use for Testing , Press 1 for Chrome and 2 Firefox: ")
        if (os_name == 'Darwin') and (selected_browser =="1"):
            selected_driver = os.path.abspath(current_path+"/Drivers/Chromedriver/chromedriver_mac")
        elif (os_name == 'Darwin') and (selected_browser =="2"):
            selected_driver = os.path.abspath(current_path+"/Drivers/geckodriver/geckodriver_mac")
        elif (os_name == 'Linux') and (selected_browser =="1"):
            selected_driver = os.path.abspath(current_path+"/Drivers/Chromedriver/chromedriver_linux")
        elif (os_name == 'Linux') and (selected_browser =="2"):
            selected_driver = os.path.abspath(current_path+"/Drivers/geckdriver/geckodriver_linux")
        else:
            print("No Driver is there")
        if selected_browser == "1":
           self.driver =  webdriver.Chrome(executable_path= selected_driver)
        elif selected_browser =="2":
            self.driver = webdriver.Firefox(executable_path=selected_driver)
        else:
            raise AssertionError("There is no Driver Defined")
        print("Connection has been stated on " + str(datetime.datetime.now()))
        print("Environment has been Setup")
        self.driver.maximize_window()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://localhost:8080/")

    def tearDown(self):
        if (self.driver != None):
            print("--------------------------------------")
            print("Test Environment is Destroyed")
            print("Run Completed at " + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()


