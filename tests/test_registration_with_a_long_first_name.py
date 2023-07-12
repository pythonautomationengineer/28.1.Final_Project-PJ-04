from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from generators.very_long_first_name import very_long_first_name_generation
from settings import link, password, unused_phone


def test_valid_registration(browser):
    """Регистрация со всеми валидными полями кроме имени (слишком длинное имя)"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    # Имя
    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(very_long_first_name_generation())

    # Фамилия
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(''))

    # Номер
    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    # Пароли
    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    # Кнопка регистрации
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста о том, что валидная длина имени от 2 до 30 символов
    WebDriverWait(browser, 5)
    text_information = browser.find_element(*Selectors.FIRST_NAME_ERROR_TEXT)

    assert text_information.is_displayed()

    print()
    print()
    print(f"Текст '{text_information.text}' найден на странице, значит при регистрации "
          f"было введено слишком длинное имя, так как Имя было введено полностью кириллическое")
