import time

from environmental_setup import environmental_setup
from Locators.Owner_page_locator import *
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Owner_Page_Methods(environmental_setup):
    first_name = 'Taimoor'
    last_name = 'Pasha'
    city_name = 'London'
    address = '401 Gable Roads'
    telephone = '+8190289765'

    def lastname_field_presence(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        try:
            last_name_field = driver.find_element_by_id(last_name_field_id)
            if last_name_field.is_displayed():
                print("Last Name Field is Displaying")
        except:
            raise AssertionError("Last Name Field is not Displaying")

    def submit_button_presence(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        search_owner_button = driver.find_element_by_xpath(search_owner_button_xpath)
        try:
            if search_owner_button.is_displayed():
                print("Search Owner Button is Displaying.")
        except:
            raise AssertionError("Serach Owner Button is not Displaying.")


    def add_owner_button(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        try:
            add_owner_button = driver.find_element_by_xpath(new_owner_button_xpath)
            if add_owner_button.is_displayed():
                print("Add New Owner Button is Displaying")
        except:
            raise AssertionError("Add New Owner Button is not Displaying.")

    def verify_all_texts_displaying(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/new")
        owners_page_texts_list = [owner_first_name_text_xpath, owner_last_name_text_xpath,
                                  address_text_xpath, telephone_text_xpath, city_text_xpath]
        owners_page_texts_elements = [driver.find_element_by_xpath(e) for e in owners_page_texts_list]
        global i
        try:
            for i in range(0, len(owners_page_texts_elements), 2):
                if owners_page_texts_elements[i].is_displayed():
                    print(str(owners_page_texts_elements[i].get_attribute('value'))+" Text is displaying")
        except:
            raise AssertionError(str(owners_page_texts_elements[i].get_attribute('value'))+" Text is not displaying")

    def verify_all_fields_displaying(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/new")
        owners_page_fields_list = [owner_first_name_field_id, owner_last_name_field_id,
                                   owner_address_field_id, owner_telephone_field_id, owner_city_field_id]
        owners_page_fields_elements = [driver.find_element_by_id(e) for e in owners_page_fields_list]
        global i
        try:
            for i in range(0, len(owners_page_fields_elements), 2):
                if owners_page_fields_elements[i].is_displayed():
                    print(str(owners_page_fields_elements[i].get_attribute('name')) + " is displaying")
        except:
            raise AssertionError(str(owners_page_fields_elements[i].get_attribute('name')) + " is not displaying")

    def enter_values_text_fields(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/new")
        first_name_field = driver.find_element_by_id(owner_first_name_field_id)
        last_name_field = driver.find_element_by_id(owner_last_name_field_id)
        city_field = driver.find_element_by_id(owner_city_field_id)
        address_field = driver.find_element_by_id(owner_address_field_id)
        telephone_field = driver.find_element_by_id(owner_telephone_field_id)
        first_name_field.send_keys(self.first_name)
        last_name_field.send_keys(self.last_name)
        city_field.send_keys(self.city_name)
        address_field.send_keys(self.address)
        telephone_field.send_keys(self.telephone)
        all_fields = driver.find_elements_by_xpath(all_text_fields_class_xpath)
        data_entered = []
        for i in all_fields:
            data_entered.append(i.get_attribute('value'))
        fields_names = []
        for i in all_fields:
            fields_names.append(i.get_attribute('name'))
        data_dict = dict(zip(fields_names,data_entered))
        for name, age in data_dict.items():
            if age == '':
                print("Data has not been Entered at "+name+" field.")
        if '' not in data_entered:
            print("Data has been Entered on all Fields")
        else:
            raise AssertionError("Data has not been entered on all fields")
        return data_dict

    def create_new_owner(self):
        adding_values = self.enter_values_text_fields()
        driver = self.driver
        add_new_owner_button = driver.find_element_by_xpath(add_newowner_button_xpath)
        add_new_owner_button.click()
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, Owner_Information_header_xpath)))
        owner_name_text = driver.find_element_by_xpath(owners_name_xpath).text
        owner_address_text = driver.find_element_by_xpath(owners_address_xpath).text
        owner_city_text = driver.find_element_by_xpath(owners_city_xpath).text
        owner_telephone_text = driver.find_element_by_xpath(owners_telephone_xpath).text
        if owner_name_text == (self.first_name+" "+self.last_name):
            print('Name is correct')
        else:
            ValueError ('Name is not Correct')

        if owner_address_text == self.address:
            print('Address is Correct')
        else:
            ValueError ("Address is not Corrct")

        if owner_city_text == self.city_name:
            print('City is correct')
        else:
            ValueError('City is not correct')

        if owner_telephone_text == self.telephone:
            print('Telephone is correct')
        else:
            ValueError('Telephone is not correct')
