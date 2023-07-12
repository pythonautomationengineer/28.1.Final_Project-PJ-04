from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert
from Classes.try_except_exception import handle_captcha
from settings import link, login, password


def test_login(browser):
    """Вход в личный кабинет по валидному логину и паролю"""
    browser.get(link)

    # Явное ожидание таба с текстом "Логин"
    wait = WebDriverWait(browser, 7)
    login_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_LOGIN_LOGIN))
    login_button.click()

    # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без ошибок
    handle_captcha(browser)

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(login)
    password_input.send_keys(password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

    print()
    print()
    print(f'Вход успешно выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице.')
