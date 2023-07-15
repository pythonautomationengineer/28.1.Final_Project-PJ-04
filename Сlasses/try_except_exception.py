from selenium.common.exceptions import NoSuchElementException
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert


def handle_captcha(browser):
    """На случай появления каптчи на сайте"""
    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), DataForAssert.CAPTCHA_INFO
    except NoSuchElementException:
        pass
