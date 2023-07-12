from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert
from Classes.try_except_exception import handle_captcha
from settings import link, email_valid, password


def test_login(browser):
    """Вход в личный кабинет по валидному email и паролю"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 7)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
    email_button.click()

    # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без ошибок
    handle_captcha(browser)

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(email_valid)
    password_input.send_keys(password)

    # Кнопка "Войти"
    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

    print()
    print()
    print(f'Вход успешно выполнен. Необходимый текст "{DataForAssert.CREDENTIALS}" присутствует на странице')
