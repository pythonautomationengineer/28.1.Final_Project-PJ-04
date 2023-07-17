import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    # Создание объекта ChromeOptions
    chrome_options = Options()

    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-extensions")

    # chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(chrome_options)
    browser.maximize_window()

    yield browser
    browser.delete_all_cookies()
    browser.quit()
