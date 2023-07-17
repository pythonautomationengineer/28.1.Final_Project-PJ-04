import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def browser():
    # Создание объекта ChromeOptions
    chrome_options = Options()

    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-extensions")

    # chrome_options.add_argument("--headless")

    # Получение пути к актуальному WebDriver
    driver_path = ChromeDriverManager().install()

    # Создание экземпляра Service с указанием пути к WebDriver
    service = Service(driver_path)

    # Создание экземпляра WebDriver с использованием Service
    browser = webdriver.Chrome(service=service, options=chrome_options)
    browser.maximize_window()

    yield browser
    browser.delete_all_cookies()
    browser.quit()
