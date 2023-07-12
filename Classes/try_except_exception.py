from selenium.common.exceptions import NoSuchElementException
from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert


def handle_captcha(browser):
    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), DataForAssert.CAPTCHA_INFO
    except NoSuchElementException:
        pass
