from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from settings import link, unused_phone
from Classes.Data_for_Assert import DataForAssert
from generators.Characters_generator import CharactersGenerator


def test_big_letter(browser):
    """Появление сообщения в форме регистрации с текстом "Пароль должен содержать хотя бы одну заглавную букву"
    под полем "Пароль" и "Подтверждение пароля" при введении 8 символов: маленьких букв и цифр"""
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
    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
        CharactersGenerator.small_letter_password_generator())
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
        CharactersGenerator.small_letter_password_generator())

    # Кнопка "Зарегистрироваться"
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста Пароль должен содержать хотя бы одну заглавную букву" под полем 'Пароль'"
    WebDriverWait(browser, 2)
    text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD)

    # Явное ожидание текста "Пароль должен содержать хотя бы одну заглавную букву" под полем 'Подтверждение пароля'"
    WebDriverWait(browser, 2)
    text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

    assert text_information.text == DataForAssert.BIG_LETTER_TEXT_IN_PASSWORD \
           and text_information_2.text == DataForAssert.BIG_LETTER_TEXT_IN_PASSWORD

    print()
    print()
    print(
        f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке 'Зарегистрироваться'. "
        f"Значит валидация на заглавную букву пароля работает")
