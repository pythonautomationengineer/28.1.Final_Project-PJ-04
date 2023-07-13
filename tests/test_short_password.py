from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert
from Classes.FakePerson import FakePerson
from generators.Characters_generator import CharactersGenerator
from settings import link, unused_phone


def test_short_password(browser):
    """Появление сообщения в форме регистрации с текстом "Длина пароля должна быть не менее 8 символов"
    под полем "Новый пароль" при вводе пароля из 7 символов"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    # Имя
    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(''))

    # Фамилия
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(''))

    # Телефон
    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    # Пароли
    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(CharactersGenerator.short_password_generator())
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
        CharactersGenerator.short_password_generator())

    # Кнопка "Зарегистрироваться"
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста "Длина пароля должна быть не менее 8 символов" под полем 'Пароль'"
    WebDriverWait(browser, 3)
    text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

    # Явное ожидание текста "Длина пароля должна быть не менее 8 символов" под полем 'Подтверждение пароля'"
    WebDriverWait(browser, 3)
    text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

    assert text_information.text == DataForAssert.VERY_SHORT_PASSWORD \
           and text_information_2.text == DataForAssert.VERY_SHORT_PASSWORD

    print()
    print()
    print(
        f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке 'Зарегистрироваться'. "
        f"Значит валидация на короткое значение пароля работает")
