from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert
from settings import link, phone_valid, password


def test_phone_tabs(browser):
    """Смена таба выбора аутентификации при вводе телефона в табе 'Почта'"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 7)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
    email_button.click()

    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), DataForAssert.CAPTCHA_INFO
    except NoSuchElementException:
        pass

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(phone_valid)
    password_input.send_keys(password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS
    print()
    print()
    print(f'Вход в кабинет выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице, значит автоматическая '
          f'смена таба произошла.')
