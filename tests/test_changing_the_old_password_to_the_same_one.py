from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from Classes.Data_for_Assert import DataForAssert
from settings import link, email_valid, password

def test_login(browser):
    """Невозможность изменения старого пароля на новый, если он полностью совпадает со старым"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 7)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
    email_button.click()

    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), DataForAssert.CAPTCHA_INFO
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

    # Иконка "карандаш" для смены пароля
    browser.find_element(*Selectors.CHANGING_PASSWORD_ICON).click()

    # Явное ожидание поля ввода текущего пароля
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(Selectors.CURRENT_PASSWORD))

    # Текущий пароль
    browser.find_element(*Selectors.CURRENT_PASSWORD).click()
    browser.find_element(*Selectors.CURRENT_PASSWORD).send_keys(password)

    # Новый пароль
    browser.find_element(*Selectors.NEW_PASSWORD).click()
    browser.find_element(*Selectors.NEW_PASSWORD).send_keys(password)

    # Подтверждение нового пароля
    browser.find_element(*Selectors.CONFIRM_PASSWORD).click()
    browser.find_element(*Selectors.CONFIRM_PASSWORD).send_keys(password)

    # Сохранение нового пароля
    browser.find_element(*Selectors.PASSWORD_SAVE).click()

    wait = WebDriverWait(browser, 5)
    wait.until(EC.visibility_of_element_located(Selectors.USER_PASSWORD_EDITOR_ERROR_TEXT))

    find_text = browser.find_element(*Selectors.USER_PASSWORD_EDITOR_ERROR_TEXT).text

    assert find_text == DataForAssert.PREVIOUSLY_USED_PASSWORD

    print()
    print()
    print(f'Текст "{find_text}" найден на странице, значит текущий пароль изменить на тот же самый нельзя')
