from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from settings import link, email_valid, password
from Classes.FakePerson import FakePerson
from Classes.CSS_Selectors import Selectors


def test_return_to_home(browser):
    """Возвращение на главную страницу из модального окна с текстом 'Учетная запись уже используется'"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    # Имя
    browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(None))

    # Фамилия
    browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(None))

    # email
    browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
    browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    # Кнопка "Зарегистрироваться"
    browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    # Явное ожидание кнопки "Войти" в модальном окне под заголовком 'Учетная запись уже используется'

    WebDriverWait(browser, 5)
    return_button = wait.until(EC.visibility_of_element_located(Selectors.RETURN_BUTTON))

    assert return_button.is_displayed()

    print()
    print()
    print(f"По кнопке 'Войти' в модальном окне под заголовком 'Учетная запись уже используется' можно вернуться на "
          f"главную страницу")
