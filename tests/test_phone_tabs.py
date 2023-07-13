from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.try_except_exception import handle_captcha
from settings import link, phone_valid, password


def test_phone_tabs(browser):
    """Смена таба выбора аутентификации при вводе телефона в табе 'Почта'"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 10)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
    email_button.click()

    # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без ошибок
    handle_captcha(browser)

    # Телефон и пароль
    browser.find_element(*Selectors.USERNAME_INPUT).send_keys(phone_valid)
    browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

    # Кнопка "Войти"
    browser.find_element(*Selectors.LOGIN_BUTTON).click()

    assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS
    print()
    print()
    print(f'Вход в кабинет выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице, значит автоматическая '
          f'смена таба произошла.')
