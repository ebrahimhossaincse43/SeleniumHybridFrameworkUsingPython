from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Current session is {}".format(driver.session_id))
    return driver
