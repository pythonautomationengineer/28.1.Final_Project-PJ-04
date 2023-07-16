import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from settings import link, phone_valid, old_password, login, password, email_valid
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.Stability import Captcha


# запустить все тесты в этом модуле
# pytest -k 'personal' -v -s

class TestLoginPositive:
    """Позитивные тесты, которые проверяют вход в личный кабинет"""

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_valid_phone_and_password(browser):
        """Вход в личный кабинет по валидному телефону и паролю"""
        browser.get(link)

        # Явное ожидание таба с текстом "Телефон"
        wait = WebDriverWait(browser, 7)
        phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
        phone_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Телефон и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(phone_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

        # Кнопка "Войти"
        browser.find_element(*Selectors.LOGIN_BUTTON).click()

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице.')

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_valid_email_and_password(browser):
        """Вход в личный кабинет по валидному email и паролю"""
        browser.get(link)

        # Явное ожидание таба с текстом "Почта"
        wait = WebDriverWait(browser, 7)
        email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
        email_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # email и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(email_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

        # Кнопка "Войти"
        login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
        login_button.click()

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Необходимый текст "{DataForAssert.CREDENTIALS}" присутствует на странице.')

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_valid_login_and_password(browser):
        """Вход в личный кабинет по валидному логину и паролю"""
        browser.get(link)

        # Явное ожидание таба с текстом "Логин"
        wait = WebDriverWait(browser, 7)
        login_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_LOGIN_LOGIN))
        login_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Логин и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(login)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

        # Кнопка "Войти"
        browser.find_element(*Selectors.LOGIN_BUTTON).click()

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице.')

    @staticmethod
    @pytest.mark.xfail
    def test_email_tabs(browser):
        """Смена таба выбора аутентификации при вводе почты в табе "Телефон"""
        browser.get(link)

        # Явное ожидание таба с текстом "Телефон"
        wait = WebDriverWait(browser, 7)
        phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
        phone_button.click()

        username_input = browser.find_element(*Selectors.USERNAME_INPUT)
        password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод email
        username_input.send_keys(email_valid)

        # Клик по полю "Пароль"
        password_input.click()

        # Ввод пароля в поле "Пароль"
        password_input.send_keys(password)

        # Клик по кнопке "Войти"
        browser.find_element(*Selectors.LOGIN_BUTTON).click()

        # Явное ожидание сообщения с текстом ошибки
        wait = WebDriverWait(browser, 3)
        error_message = wait.until(EC.visibility_of_element_located(Selectors.FORM_ERROR_MESSAGE))

        assert error_message.text == DataForAssert.ERROR_LOGIN_AND_PASSWORD_TEXT
        print()
        print()
        print(f'Вход в кабинет не выполнен, так как на странице появился текст ошибки "{error_message.text}". '
              f'Смена таба не произошла.')

    @staticmethod
    @pytest.mark.xfail
    def test_phone_tabs(browser):
        """Смена таба выбора аутентификации при вводе телефона в табе 'Почта'"""
        browser.get(link)

        # Явное ожидание таба с текстом "Почта"
        wait = WebDriverWait(browser, 10)
        email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
        email_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Телефон и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(phone_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

        # Кнопка "Войти"
        browser.find_element(*Selectors.LOGIN_BUTTON).click()

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS
        print()
        print()
        print(f'Вход в кабинет выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице, значит автоматическая '
              f'смена таба произошла.')


class TestLoginNegative:
    """Негативные тесты, которые проверяют вход в личный кабинет"""

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_old_password(browser):
        """Вход в ЛК с предыдущем паролем"""
        browser.get(link)

        # Явное ожидание таба с текстом "Телефон"
        wait = WebDriverWait(browser, 7)
        phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
        phone_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Телефон и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(phone_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(old_password)

        # Кнопка "Войти"
        login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
        login_button.click()

        # Текст ошибки входа
        wait = WebDriverWait(browser, 3)
        wait.until(EC.visibility_of_element_located(Selectors.FORM_ERROR_MESSAGE))
        error_message = browser.find_element(*Selectors.FORM_ERROR_MESSAGE).text

        assert error_message == DataForAssert.ERROR_LOGIN_AND_PASSWORD_TEXT

        print()
        print()
        print(f'Появилась ошибка входа с текстом "{error_message}". Вход не может быть выполнен с предыдущим паролем."')
