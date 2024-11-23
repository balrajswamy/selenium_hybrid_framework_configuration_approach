import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
user_email = os.getenv("user_email")
user_pwd = os.getenv("user_pwd")

@pytest.fixture()
def setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    yield
    driver.quit()

@allure.title("TestCase#1 to Test a Login with Valid Credentials")
def test_Login_with_valid_credentials(setup_and_teardown):
    print("1. Running with valid email/password!")

    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(user_email)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(user_pwd)
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(1)
    assert driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed(), "Login is failed!"


def generate_invalid_email_with_time_stamp():
    from datetime import datetime

    today = datetime.now().strftime("%d%m%Y%H%M%S")
    invalid_email = "test_software_"+str(today)+"@gmail.com"
    return invalid_email

@allure.title("TestCase#2 to Test a Login with InValid email and Valid password Credentials")
def test_login_invalid_email_with_valid_password(setup_and_teardown):
    print("2. Running with invalid_email_valid_password!")

    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)

    invalid_email = generate_invalid_email_with_time_stamp()

    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(invalid_email)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys(user_pwd)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(3)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    warning_message = driver.find_element(By.XPATH,'//div[@id="account-login"]/div[1]').text
    #print("warning_message=>", warning_message)
    assert warning_message.__contains__(expected_warning_message), f"Login is failed due to {expected_warning_message}!"
    time.sleep(1)


@allure.title("TestCase#2 to Test a Login with Valid email with invalid password Credentials")
def test_login_valid_email_with_invalid_password(setup_and_teardown):
    print("3. Running with valid_email_invalid_password!")

    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(user_email)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(1)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    warning_message = driver.find_element(By.XPATH, '//div[@id="account-login"]/div[1]').text
    # print("warning_message=>", warning_message)
    assert warning_message.__contains__(expected_warning_message), f"Login is failed due to {expected_warning_message}!"
    time.sleep(1)


@allure.title("TestCase#3 to Test a Login with without entering any Credentials")
def test_login_without_entering_credentials(setup_and_teardown):
    print("4. Running without entering credentials")

    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"Login").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(3)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    warning_message = driver.find_element(By.XPATH, '//div[@id="account-login"]/div[1]').text
    # print("warning_message=>", warning_message)
    assert warning_message.__contains__(expected_warning_message), f"Login is failed due to {expected_warning_message}!"
    time.sleep(1)
