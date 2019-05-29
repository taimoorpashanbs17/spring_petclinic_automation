from environmental_setup import *
from Locators.Owner_page_locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Scripts.Owner_Page_Methods import Owner_Page_Methods as owner_page
import time

class Owner_Search__Page_Methods(environmental_setup):
    def test_1_search_owners(self, lastname):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        last_name_field = driver.find_element_by_id(last_name_field_id)
        last_name_field.send_keys(lastname)
        search_owner_button = driver.find_element_by_xpath(search_owner_button_xpath)
        search_owner_button.click()
        try:
            alert_message = driver.find_element_by_xpath(search_notfound_alert_xpath)
            if alert_message.is_displayed():
                print(lastname + " " + alert_message.text)
        except:
            WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, Owner_Information_header_xpath)))
            owner_name_text = driver.find_element_by_xpath(owners_name_xpath).text
            owner_address_text = driver.find_element_by_xpath(owners_address_xpath).text
            owner_city_text = driver.find_element_by_xpath(owners_city_xpath).text
            owner_telephone_text = driver.find_element_by_xpath(owners_telephone_xpath).text
            if owner_name_text == (owner_page.first_name + " " + owner_page.last_name):
                print('Name is correct')
            else:
                ValueError('Name is not Correct')

            if owner_address_text == owner_page.address:
                print('Address is Correct')
            else:
                ValueError("Address is not Corrct")

            if owner_city_text == owner_page.city_name:
                print('City is correct')
            else:
                ValueError('City is not correct')

            if owner_telephone_text == owner_page.telephone:
                print('Telephone is correct')
            else:
                ValueError('Telephone is not correct')

    def test_2_verify_data_edit(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        last_name_field = driver.find_element_by_id(last_name_field_id)
        last_name_field.send_keys(owner_page.last_name)
        search_owner_button = driver.find_element_by_xpath(search_owner_button_xpath)
        search_owner_button.click()
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, Owner_Information_header_xpath)))
        edit_button = driver.find_element_by_xpath(edit_owner_xpath)
        edit_button.click()
        first_name_field = driver.find_element_by_id(owner_first_name_field_id)
        last_name_field = driver.find_element_by_id(owner_last_name_field_id)
        city_field = driver.find_element_by_id(owner_city_field_id)
        address_field = driver.find_element_by_id(owner_address_field_id)
        telephone_field = driver.find_element_by_id(owner_telephone_field_id)
        if first_name_field.get_attribute('value') == owner_page.first_name:
            print("First Name is Same")
        else:
            raise ValueError("First name is not Same")
        if last_name_field.get_attribute('value') == owner_page.last_name:
            print("Last Name is Same")
        else:
            raise ValueError("Last name is not Same")
        if city_field.get_attribute('value') == owner_page.city_name:
            print("City is Same")
        else:
            raise ValueError("City name is not Same")
        if address_field.get_attribute('value') == owner_page.address:
            print("Address is Same")
        else:
            raise ValueError("Address name is not Same")
        if telephone_field.get_attribute('value') == owner_page.telephone:
            print("Telephone is Same")
        else:
            raise ValueError("Telephone is not Same")

    def test_3_update_data_fields(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        last_name_field = driver.find_element_by_id(last_name_field_id)
        last_name_field.send_keys(owner_page.last_name)
        search_owner_button = driver.find_element_by_xpath(search_owner_button_xpath)
        search_owner_button.click()
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.XPATH, Owner_Information_header_xpath)))
        edit_button = driver.find_element_by_xpath(edit_owner_xpath)
        edit_button.click()
        first_name_field = driver.find_element_by_id(owner_first_name_field_id)
        last_name_field = driver.find_element_by_id(owner_last_name_field_id)
        city_field = driver.find_element_by_id(owner_city_field_id)
        address_field = driver.find_element_by_id(owner_address_field_id)
        telephone_field = driver.find_element_by_id(owner_telephone_field_id)
        first_name_field.clear()
