from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from settings import link, phone_valid, old_password


def test_login(browser):
    """Вход в ЛК с предыдущем паролем"""
    browser.get(link)

    # Явное ожидание таба с текстом "Телефон"
    wait = WebDriverWait(browser, 5)
    phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
    phone_button.click()

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(phone_valid)
    password_input.send_keys(old_password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(Selectors.FORM_ERROR_MESSAGE))
    error_message = browser.find_element(*Selectors.FORM_ERROR_MESSAGE).text

    assert error_message == 'Неверный логин или пароль'

    print()
    print()
    print(f'Появилась ошибка входа с текстом "{error_message}". Вход не может быть выполнен с предыдущим паролем."')
