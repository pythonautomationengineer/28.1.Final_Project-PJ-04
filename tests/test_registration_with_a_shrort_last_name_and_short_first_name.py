from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from generators.one_symbol_generator import one_symbol_generator
from settings import link, password, additional_number


def test_valid_registration(browser):
    """Регистрация со всеми валидными полями кроме фамилии и имени (слишком короткая фамилия и имя)"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    first_name = one_symbol_generator()

    # Имя
    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(first_name)

    # Фамилия
    last_name = one_symbol_generator()
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(last_name)

    # Телефон
    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(additional_number)

    # Пароли
    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    # Кнопка регистрации
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста о том, что валидная длина фамилии от 2 до 30 символов
    WebDriverWait(browser, 5)

    # Текст ошибки под полем с фамилией
    text_information = browser.find_element(*Selectors.LAST_NAME_ERROR_TEXT)

    # Текст ошибки под полем имени
    text_information_2 = browser.find_element(*Selectors.FIRST_NAME_ERROR_TEXT)

    assert text_information.is_displayed() and text_information_2.is_displayed()

    print()
    print()
    print(f"Текст '{text_information.text}' найден на странице в 2 местах, "
          f"значит при регистрации была введена слишком короткая Фамилия и слишком короткое Имя")
