from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def generate_invalid_email_with_time_stamp():
    from datetime import datetime

    today = datetime.now().strftime("%d%m%Y%H%M%S")
    invalid_email = "test_software_"+str(today)+"@gmail.com"
    return invalid_email
def test_register_with_mandatory_fields():
    print("1. Running with mandatory fields")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
    invalid_email = generate_invalid_email_with_time_stamp()
    password = "Balraj@2020"
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(invalid_email)
    driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("9952481537")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys(password)
    driver.find_element(By.XPATH,"//input[@name='newsletter' and @value = '1']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(3)
    success_message = driver.find_element(By.XPATH, "//div[@id='content']/h1").text
    assert success_message.__contains__("Your Account Has Been Created!")
    print("success_message=>", success_message)

    time.sleep(3)
    driver.quit()

def test_register_with_new_email_password():
    print("2. Running with new email/password")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
    invalid_email = generate_invalid_email_with_time_stamp()
    password = "Balraj@2020"
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys(invalid_email)
    driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("9952481537")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys(password)
    driver.find_element(By.XPATH,"//input[@name='newsletter' and @value = '1']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(3)
    success_message = driver.find_element(By.XPATH, "//div[@id='content']/h1").text
    assert success_message.__contains__("Your Account Has Been Created!")
    print("success_message=>", success_message)

    time.sleep(3)
    driver.quit()


def test_register_with_existing_email():
    print("3. Running with existing email/password")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Balraj")
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Ponnuswamy")
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("balrajswamy@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("9952481537")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Balraj@2020")
    driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("Balraj@2020")
    driver.find_element(By.XPATH,"//input[@name='newsletter' and @value = '1']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text
    assert error_message.__contains__("Warning: E-Mail Address is already registered!")
    print("Error_message=>", error_message)

    time.sleep(3)
    driver.quit()


def test_register_without_entering_any_fields():
    print("4. Running with existing email/password")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("")


    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("")


    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")


    driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("")
    driver.find_element(By.XPATH, "//input[@name='confirm']").send_keys("")

    #driver.find_element(By.XPATH, "//input[@name='agree' and @value = '1']").click()

    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text
    print("Error_message=>", error_message)

    policy_warning_message = "Warning: You must agree to the Privacy Policy!"
    assert error_message.__contains__(policy_warning_message),"All the fields must be entered!"

    expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
    assert driver.find_element(By.XPATH, '//input[@name="firstname"]/following-sibling::div').text.__eq__(
        expected_firstname_warning_message)

    expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
    assert driver.find_element(By.XPATH, '//input[@name="lastname"]/following-sibling::div').text.__eq__(
        expected_lastname_warning_message)

    expected_email_warning_message="E-Mail Address does not appear to be valid!"
    assert driver.find_element(By.XPATH, '//input[@name="email"]/following-sibling::div').text.__eq__(
        expected_email_warning_message)

    expected_telephone_warning_message="Telephone must be between 3 and 32 characters!"
    assert driver.find_element(By.XPATH, '//input[@name="telephone"]/following-sibling::div').text.__eq__(
        expected_telephone_warning_message)

    expected_password_warning_message = "Password must be between 4 and 20 characters!"
    assert driver.find_element(By.XPATH, '//input[@name="password"]/following-sibling::div').text.__eq__(
        expected_password_warning_message)

    time.sleep(3)
    driver.quit()

