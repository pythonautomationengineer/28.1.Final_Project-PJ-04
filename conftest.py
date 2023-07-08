import pytest
from selenium import webdriver


# @pytest.fixture
# def browser():
#     options = webdriver.ChromeOptions()
#     options.add_argument('--headless')  # запуск браузера без GUI
#
#     browser = webdriver.Chrome(executable_path='chrome.exe', options=options)  # драйвер находится в Path на Windows
#     browser.maximize_window()
#     yield browser
#     browser.quit()


@pytest.fixture
def browser():
    browser = webdriver.Chrome(executable_path='chrome.exe')
    browser.maximize_window()
    yield browser
    browser.delete_all_cookies()
    browser.quit()
