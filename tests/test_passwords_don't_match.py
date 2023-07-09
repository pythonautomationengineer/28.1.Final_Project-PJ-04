from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from generators.valid_psswrds_but_dont_match_generator import p_password_generator, p2_password_generator
from settings import link, unused_phone


def test_pass_dont_match(browser):
    """Выводится "Пароли не совпадают" под полем "Подтверждение пароля", если пользователь ввел разные пароли
    при регистрации"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(None))
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(None))

    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    password_1 = p_password_generator()
    password_2 = p2_password_generator()
    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password_1)
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password_2)

    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста "Пароли не совпадают" под полем 'Подтверждение пароля'"
    WebDriverWait(browser, 2)
    text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

    assert text_information_2.text == 'Пароли не совпадают'

    print()
    print()
    print(
        f"Текст '{text_information_2.text}' найден на странице под полем 'Подтверждение пароля' после клика по кнопке "
        f"'Зарегистрироваться'. Значит валидация на подтверждение пароля работает")
