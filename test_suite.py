import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Action_page.Action import LoginPage


# Fixture to launch browser
@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

# Fixture to perform login
@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page("https://www.saucedemo.com/")

def test_login_page(login):
    login.enter_username("standard_user")

