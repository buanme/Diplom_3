import os
import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.restore_password_page import RestorePasswordPage

browser = os.environ.get('browser') or 'chrome'

class WebDriverFactory:
    @staticmethod
    def get_web_driver(browser_name):
        if browser_name == 'chrome':
            return webdriver.Chrome()
        elif browser_name == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

@pytest.fixture
def driver():
    driver = WebDriverFactory.get_web_driver(browser)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)

@pytest.fixture
def login_page(driver, wait):
    return LoginPage(driver, wait)

@pytest.fixture
def feed_page(driver, wait):
    return FeedPage(driver, wait)

@pytest.fixture
def main_page(driver, wait):
    return MainPage(driver, wait)

@pytest.fixture
def personal_account_page(driver, wait):
    return PersonalAccountPage(driver, wait)

@pytest.fixture
def restore_password_page(driver, wait):
    return RestorePasswordPage(driver, wait)
