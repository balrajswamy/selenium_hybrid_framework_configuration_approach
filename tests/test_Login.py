import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_Login_with_valid_credentials():
    print("1. Running with valid email/password!")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH,'//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)

    driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("balrajswamy@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("Balraj@2020")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@value='Login']").click()
    time.sleep(1)
    assert driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed(), "Login is failed!"
    driver.quit()

def generate_invalid_email_with_time_stamp():
    from datetime import datetime

    today = datetime.now().strftime("%d%m%Y%H%M%S")
    invalid_email = "test_software_"+str(today)+"@gmail.com"
    return invalid_email


def test_login_invalid_email_with_valid_password():
    print("2. Running with invalid_email_valid_password!")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)

    invalid_email = generate_invalid_email_with_time_stamp()

    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(invalid_email)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("Balraj@2020")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(3)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    warning_message = driver.find_element(By.XPATH,'//div[@id="account-login"]/div[1]').text
    #print("warning_message=>", warning_message)
    assert warning_message.__contains__(expected_warning_message), f"Login is failed due to {expected_warning_message}!"
    time.sleep(1)
    driver.quit()


def test_login_valid_email_with_invalid_password():
    print("3. Running with valid_email_invalid_password!")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(1)
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("balrajswamy@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("balraj@2020")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    time.sleep(1)
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    warning_message = driver.find_element(By.XPATH, '//div[@id="account-login"]/div[1]').text
    # print("warning_message=>", warning_message)
    assert warning_message.__contains__(expected_warning_message), f"Login is failed due to {expected_warning_message}!"
    time.sleep(1)
    driver.quit()


def test_login_without_entering_credentials():
    print("4. Running without entering credentials")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
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
    driver.quit()