from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from settings import link, password, unused_phone


def test_valid_registration(browser):
    """Отправка сайтом кода подтверждения регистрации при всех введенных валидных данных, которые ранее
    не были использованы"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 5)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    # Имя
    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(''))

    # Фамилия
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(''))

    # Номер
    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    # Кнопка "Зарегистрироваться"
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста о том, что код подтверждения телефона был отправлен по указанному номеру
    WebDriverWait(browser, 5)
    text_information = browser.find_element(*Selectors.CONFIRMATION_PHONE_TEXT)

    assert text_information.is_displayed()

    print()
    print()
    print(f"Текст '{text_information.text}' найден на странице, значит пользователю "
          f"код подтверждения телефона был отправлен")
