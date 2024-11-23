import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import ReadConfiguration

@pytest.fixture()
def setup_and_teardown(request):
    #global driver
    driver = None

    browser = ReadConfiguration.reading_config("basic_info","browser")
    base_url = ReadConfiguration.reading_config("basic_info","base_url")
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        print("Provide a valid browser name from the list chrome/firefox/edge")
    #driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()