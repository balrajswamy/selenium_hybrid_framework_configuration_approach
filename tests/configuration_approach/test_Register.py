from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
user_email = os.getenv("user_email")
user_pwd = os.getenv("user_pwd")
user_phone = os.getenv('user_phone')


@pytest.mark.usefixtures('setup_and_teardown')
class TestRegister:
    def generate_invalid_email_with_time_stamp(self):
        from datetime import datetime

        today = datetime.now().strftime("%d%m%Y%H%M%S")
        self.invalid_email = "test_software_"+str(today)+"@gmail.com"
        return self.invalid_email

    @allure.title("TestCase#1 to register with mandary fields!")
    @allure.description("Filling all the mandatory fields")
    def test_register_with_mandatory_fields(self):
        print("1. Running with mandatory fields")

        time.sleep(1)
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
        invalid_email = self.generate_invalid_email_with_time_stamp()

        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(invalid_email)
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys(user_phone)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(user_pwd)
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys(user_pwd)
        self.driver.find_element(By.XPATH,"//input[@name='newsletter' and @value = '1']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        time.sleep(3)
        success_message = self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        assert success_message.__contains__("Your Account Has Been Created!")
        print("success_message=>", success_message)



    @allure.title("TestCase#2 to register with new email/passwords!")
    @allure.description("Filling all the mandatory fields with new email/passwords")
    def test_register_with_new_email_password(self):
        print("2. Running with new email/password")

        time.sleep(1)
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
        invalid_email = self.generate_invalid_email_with_time_stamp()

        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(invalid_email)
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys(user_phone)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(user_pwd)
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys(user_pwd)
        self.driver.find_element(By.XPATH,"//input[@name='newsletter' and @value = '1']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        time.sleep(3)
        success_message = self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
        assert success_message.__contains__("Your Account Has Been Created!")
        print("success_message=>", success_message)



    @allure.title("TestCase#3 to register with existing email/passwords!")
    @allure.description("Filling  with existing email/passwords")
    def test_register_with_existing_email(self):
        print("3. Running with existing email/password")

        time.sleep(1)
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(user_email)
        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys(user_phone)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(user_pwd)
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys(user_pwd)
        self.driver.find_element(By.XPATH,"//input[@name='newsletter' and @value = '1']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        time.sleep(3)
        error_message = self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text
        assert error_message.__contains__("Warning: E-Mail Address is already registered!")
        print("Error_message=>", error_message)



    @allure.title("TestCase#4 to without entering any fields!")
    @allure.description("Leaving as empty at fields and validating the input fields")
    def test_register_without_entering_any_fields(self):
        print("4. Running with existing email/password")

        time.sleep(1)
        self.driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("")


        self.driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("")


        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")


        self.driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("")

        #self.driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        time.sleep(3)
        error_message = self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text
        print("Error_message=>", error_message)

        policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert error_message.__contains__(policy_warning_message),"All the fields must be entered!"

        expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@name="firstname"]/following-sibling::div').text.__eq__(
            expected_firstname_warning_message)

        expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@name="lastname"]/following-sibling::div').text.__eq__(
            expected_lastname_warning_message)

        expected_email_warning_message="E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, '//input[@name="email"]/following-sibling::div').text.__eq__(
            expected_email_warning_message)

        expected_telephone_warning_message="Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@name="telephone"]/following-sibling::div').text.__eq__(
            expected_telephone_warning_message)

        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, '//input[@name="password"]/following-sibling::div').text.__eq__(
            expected_password_warning_message)

        time.sleep(3)


