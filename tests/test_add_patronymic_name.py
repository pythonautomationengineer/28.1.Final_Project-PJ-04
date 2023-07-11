from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from settings import link, email_valid, password


def test_login(browser):
    """Добавление отчества внутри личного кабинета"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 7)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
    email_button.click()

    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), 'Каптча на сайте! Придется разок войти руками в ЛК, а после запустить тест'
    except NoSuchElementException:
        pass

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(email_valid)
    password_input.send_keys(password)

    # Кнопка "Войти"
    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC))

    start_patronymic_name = browser.find_element(*Selectors.CURRENT_FIRST_NAME_AND_MIDDLE_NAME).text

    browser.find_element(*Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC).click()

    # Явное ожидание поля с текстом 'Отчество'"
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(Selectors.USER_PATRONYMIC))

    browser.find_element(*Selectors.USER_PATRONYMIC).click()

    # Ввод отчества
    browser.find_element(*Selectors.USER_PATRONYMIC).send_keys(Keys.CONTROL + "a", Keys.DELETE)
    browser.find_element(*Selectors.USER_PATRONYMIC).send_keys(
        FakePerson.generate_patronymic_name_of_man(start_patronymic_name))

    browser.find_element(*Selectors.USER_CONTACTS_EDITOR_SAVE).click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(Selectors.TEXT_INSIDE_TOAST))

    toast = browser.find_element(*Selectors.TOAST_CHANGING_NAME_LAST_NAME_PATRONYMIC)
    izm_fio = browser.find_element(*Selectors.TEXT_INSIDE_TOAST).text

    new_patronymic_name = browser.find_element(*Selectors.NEW_FIRST_NAME_AND_PATRONYMIC).text

    assert izm_fio == 'Изменение ФИО' and toast.is_displayed()

    print()
    print()
    print(f'Появилось тост-уведомление об успешном изменении отчества. '
          f'Старое отчество "{start_patronymic_name.split()[1]}" изменилось на "{new_patronymic_name.split()[1]}"')
