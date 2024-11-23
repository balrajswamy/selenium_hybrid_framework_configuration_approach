from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import allure


@allure.title("TestCase#1 to Search a valid product!")
def test_search_for_valid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,'//input[@name="search"]').send_keys("HP")
    driver.find_element(By.XPATH,'//button[contains(@class,"btn-default")]').click()
    assert driver.find_element(By.LINK_TEXT,'HP LP3065').is_displayed()
    time.sleep(3)

    driver.quit()

@allure.title("TestCase#1 to Search a Invalid product!")
def test_search_for_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,'//input[@name="search"]').send_keys("Honda")
    driver.find_element(By.XPATH,'//button[contains(@class,"btn-default")]').click()
    no_product_found = driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
    print("no_product_found=>",no_product_found)
    expect_text = "There is no product that matches the search criteria."

    assert no_product_found.__eq__(expect_text),"No text is matching!"
    time.sleep(3)

    driver.quit()

@allure.title("TestCase#3 to Search without entering any valid product!")
def test_search_without_entering_any_product_input():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,'//input[@name="search"]').send_keys()
    driver.find_element(By.XPATH,'//button[contains(@class,"btn-default")]').click()
    no_product_found = driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text
    print("no_product_found=>",no_product_found)
    expect_text = "There is no product that matches the search criteria."

    assert no_product_found.__eq__(expect_text),"No text is matching!"
    time.sleep(3)

    driver.quit()