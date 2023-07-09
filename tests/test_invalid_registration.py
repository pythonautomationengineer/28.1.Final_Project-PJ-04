from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from settings import link, email_valid, password


def test_invalid_registration(browser):
    """Регистрация по ранее используемым и действующим логином и паролем"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    # Имя
    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man())

    # Фамилия
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man())

    # email или телефон
    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    # Кнопка "Зарегистрироваться"
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание текста 'Учетная запись уже используется'
    WebDriverWait(browser, 5)
    text_information = browser.find_element(*Selectors.TEXT_ACCOUNT_RECORDS_USE_USED)

    assert text_information.is_displayed()

    print()
    print()
    print(f"Текст '{text_information.text}' найден на странице, значит пользователь с введенными данными уже есть")
