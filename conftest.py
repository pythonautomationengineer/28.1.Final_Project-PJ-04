import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    # Создание объекта ChromeOptions
    chrome_options = Options()

    # Отключение логов
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-logging")

    # Отключение расширений
    chrome_options.add_argument("--disable-extensions")

    # Включение хром-драйвера без графического интерфейса
    # chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(chrome_options)
    browser.maximize_window()

    yield browser
    browser.delete_all_cookies()
    browser.quit()
