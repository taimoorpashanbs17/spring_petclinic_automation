import time

from environmental_setup import environmental_setup
from Locators.Owner_page_locator import *
import unittest

class Owner_Page_Methods(environmental_setup):
    def test_1_lastname_field_presence(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        try:
            last_name_field = driver.find_element_by_id(last_name_field_id)
            if last_name_field.is_displayed():
                print("Last Name Field is Displaying")
        except:
            raise AssertionError("Last Name Field is not Displaying")

    def test_2_submit_button_presence(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        search_owner_button = driver.find_element_by_xpath(search_owner_button_xpath)
        try:
            if search_owner_button.is_displayed():
                print("Search Owner Button is Displaying.")
        except:
            raise AssertionError("Serach Owner Button is not Displaying.")


    def test_3_add_owner_button(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/find")
        try:
            add_owner_button = driver.find_element_by_xpath(new_owner_button_xpath)
            if add_owner_button.is_displayed():
                print("Add New Owner Button is Displaying")
        except:
            raise AssertionError("Add New Owner Button is not Displaying.")

    def test_4_verify_all_texts_displaying(self):
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

    def test_5_verify_all_fields_displaying(self):
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

    def test_6_enter_values_text_fields(self):
        driver = self.driver
        driver.get("http://localhost:8080/owners/new")
        first_name_field = driver.find_element_by_id(owner_first_name_field_id)
        last_name_field = driver.find_element_by_id(owner_last_name_field_id)
        city_field = driver.find_element_by_id(owner_city_field_id)
        address_field = driver.find_element_by_id(owner_address_field_id)
        telephone_field = driver.find_element_by_id(owner_telephone_field_id)
        first_name_field.send_keys('Taimoor')
        last_name_field.send_keys('Pasha')
        city_field.send_keys('London')
        address_field.send_keys('401 Gable Roads')
        telephone_field.send_keys('+8190289765')
        all_fields = driver.find_elements_by_xpath(all_text_fields_class_xpath)
        data_entered = []
        for i in all_fields:
            data_entered.append(i.get_attribute('value'))
        fields_names = []
        for i in all_fields:
            fields_names.append(i.get_attribute('name'))
        data_dict = dict(zip(fields_names,data_entered))
        try:
            for name, age in data_dict.items():
                if age == '':
                    print("Data has not been Entered at "+name+" field.")
        except:
            print("Data has been entered on All Fields")



if __name__ == "__main__":
    unittest.main()