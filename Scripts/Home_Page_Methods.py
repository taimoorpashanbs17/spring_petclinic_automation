from environmental_setup import environmental_setup
from Locators.Home_page_locator import *



class Home_Page_Methods(environmental_setup):

    def check_dog_image(self):
        driver = self.driver
        driver.get("http://localhost:8080/")
        dog_image = driver.find_element_by_xpath(dog_image_xpath)
        if dog_image.is_displayed():
            print('Dog Image is displaying')
        else:
            raise AssertionError("Dog Image is not Displaying")

    def check_spring_logo(self):
        driver = self.driver
        driver.get("http://localhost:8080/")
        logo_spring = driver.find_element_by_xpath(spring_stamp)
        if logo_spring.is_displayed():
            print("Logo is displaying")
        else:
            raise AssertionError("Spring Log is not displaying")

    def check_welcome_text(self):
        driver = self.driver
        driver.get("http://localhost:8080/")
        text_welcome = driver.find_element_by_xpath(welcome_text)
        if text_welcome.is_displayed():
            print("Welcome Text is displaying")
        else:
            raise AssertionError("Welcome Text is not displaying")

    def check_spring_stamp(self):
        driver = self.driver
        driver.get("http://localhost:8080/")
        stamp_spring = driver.find_element_by_xpath(spring_stamp)
        if stamp_spring.is_displayed():
            print("Spring Stamp is displaying at Bottom")
        else:
            raise AssertionError("Spring Stamp is not displaying at Bottom")

    def check_headers_texts(self):
        driver = self.driver
        driver.get("http://localhost:8080/")
        headers_text_list = [spring_stamp, spring_icon, veter_button,
                             owner_button, error_button, home_button]
        headers_texts_elements = [driver.find_element_by_xpath(e) for e in headers_text_list]
        for i in range(0, len(headers_texts_elements), 2):
            print(headers_texts_elements[i])
            if headers_texts_elements[i].is_displayed():
                print(str(headers_texts_elements[i])+" is displaying")
            else:
                raise AssertionError (str(headers_texts_elements[i])+" is not displaying")

