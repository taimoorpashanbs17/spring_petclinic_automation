from environmental_setup import environmental_setup
from Locators.Owner_page_locator import *
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .Owner_Page_Methods import Owner_Page_Methods as owner_page


class Owner_Search__Page_Methods(environmental_setup):
    def test_1_search_owners(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        last_name_field = driver.find_element_by_id(last_name_field_id)
        last_name_field.send_keys(owner_page.last_name)
        search_owner_button = driver.find_element_by_xpath(search_owner_button_xpath)
        search_owner_button.click()
        try:
            alert_message = driver.find_element_by_xpath(search_notfound_alert_xpath)
            if alert_message.is_displayed():
                print(owner_page.last_name + " " + alert_message.text)
        except:


