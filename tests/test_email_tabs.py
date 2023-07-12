from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert
from settings import link, email_valid, password


def test_email_tabs(browser):
    """Смена таба выбора аутентификации при вводе почты в табе "Телефон"""
    browser.get(link)

    # Явное ожидание таба с текстом "Телефон"
    wait = WebDriverWait(browser, 7)
    phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
    phone_button.click()

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), DataForAssert.CAPTCHA_INFO
    except NoSuchElementException:
        pass

    username_input.send_keys(email_valid)

    password_input.click()
    password_input.send_keys(password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    # Явное ожидание сообщения с текстом ошибки
    wait = WebDriverWait(browser, 3)
    error_message = wait.until(EC.visibility_of_element_located(Selectors.FORM_ERROR_MESSAGE))

    assert error_message.text == DataForAssert.ERROR_LOGIN_AND_PASSWORD_TEXT
    print()
    print()
    print(f'Вход в кабинет не выполнен, так как на странице появился текст ошибки "{error_message.text}". '
          f'Смена таба не произошла.')
