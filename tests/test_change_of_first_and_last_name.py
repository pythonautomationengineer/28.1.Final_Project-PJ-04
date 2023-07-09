from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.FakePerson import FakePerson
from settings import link, email_valid, password


def test_login(browser):
    """Изменение имени и фамилии внутри личного кабинета"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 7)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
    email_button.click()

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(email_valid)
    password_input.send_keys(password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)

    login_button.click()

    # Ожидание кнопки изменения ФИО
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC))

    # Текущая фамилия
    start_last_name = browser.find_element(*Selectors.CURRENT_LAST_NAME).text

    # Текущее имя и отчество
    start_first_name_and_middle_name = browser.find_element(*Selectors.CURRENT_FIRST_NAME_AND_MIDDLE_NAME).text
    start_first_name = start_first_name_and_middle_name.split()[0]
    # Клик по кнопке изменения ФИО
    browser.find_element(*Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC).click()

    # Явное ожидание поля с текстом 'Фамилия'"
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(Selectors.USER_LASTNAME))

    browser.find_element(*Selectors.USER_LASTNAME).click()

    # Очистить поле перед новым вводом фамилии
    browser.find_element(*Selectors.USER_LASTNAME).send_keys(Keys.CONTROL + "a", Keys.DELETE)

    # Ввод новой фамилии
    browser.find_element(*Selectors.USER_LASTNAME).send_keys(FakePerson.generate_last_name_of_man(start_last_name))

    browser.find_element(*Selectors.USER_FIRSTNAME).click()

    # Очистить поле перед новым вводом имени
    browser.find_element(*Selectors.USER_FIRSTNAME).send_keys(Keys.CONTROL + "a", Keys.DELETE)

    browser.find_element(*Selectors.USER_FIRSTNAME).send_keys(FakePerson.generate_first_name_of_man(start_first_name))

    # Сохранение нового ФИО
    browser.find_element(*Selectors.USER_CONTACTS_EDITOR_SAVE).click()

    # Ожидание toast-уведомления об успешном изменении ФИО
    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(Selectors.TEXT_INSIDE_TOAST))

    toast = browser.find_element(*Selectors.TOAST_CHANGING_NAME_LAST_NAME_PATRONYMIC)
    izm_fio = browser.find_element(*Selectors.TEXT_INSIDE_TOAST).text

    # Новое имя
    new_first_name = browser.find_element(*Selectors.NEW_FIRST_NAME_AND_PATRONYMIC).text

    # Новая фамилия
    new_last_name = browser.find_element(*Selectors.NEW_LAST_NAME).text

    assert izm_fio == 'Изменение ФИО' and toast.is_displayed()

    print()
    print()
    print(f'Toast-уведомление об изменении данных появилось на странице. Старая фамилия "{start_last_name}"'
          f' была изменена на "{new_last_name}". Старое имя "{start_first_name}"'
          f' было изменено на "{new_first_name.split()[0]}".')
