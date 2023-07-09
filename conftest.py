from selenium import webdriver
import pytest


@pytest.fixture
def browser():
    browser = webdriver.Chrome('C:\\Users\\Tagir\\Desktop\\chromedriver\\chromedriver.exe')
    browser.maximize_window()
    yield browser
    browser.delete_all_cookies()
    browser.quit()
