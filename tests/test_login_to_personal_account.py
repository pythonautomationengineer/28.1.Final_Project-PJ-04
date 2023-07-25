import pytest
from common_actions.login_to_personal_account_action_helpers import LoginHelpers
from classes.css_selectors import Selectors
from classes.data_for_assert import DataForAssert
from classes.stability import Captcha


class TestLoginPositive:
    """Позитивные тесты, которые проверяют вход в личный кабинет"""

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_valid_phone_and_password(browser):
        """Вход в личный кабинет по валидному телефону и паролю"""

        # Открытие сайта
        LoginHelpers.current_url(browser)

        # Явное ожидание таба с текстом "Телефон" и клик по нему
        LoginHelpers.wait_tab_phone_button_and_click(browser)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод валидного телефона и валидного пароля
        LoginHelpers.valid_phone_and_valid_password(browser)

        # Клик по кнопке "Войти"
        LoginHelpers.login_button(browser)

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице.')

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_valid_email_and_password(browser):
        """Вход в личный кабинет по валидному email и паролю"""
        # Открытие сайта
        LoginHelpers.current_url(browser)

        # Явное ожидание таба с текстом "Почта" и клик по нему
        LoginHelpers.wait_tab_email_button_and_click(browser)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод валидного email и пароля
        LoginHelpers.valid_email_and_valid_password(browser)

        # Клик по кнопке "Войти"
        LoginHelpers.login_button(browser)

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Необходимый текст "{DataForAssert.CREDENTIALS}" присутствует на странице.')

    @staticmethod
    @pytest.mark.xfail
    def test_login_with_valid_login_and_password(browser):
        """Вход в личный кабинет по валидному логину и паролю"""
        # Открытие сайта
        LoginHelpers.current_url(browser)

        # Явное ожидание таба с текстом "Логин" и клик по нему
        LoginHelpers.wait_tab_login_button_and_click(browser)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод валидного логина и пароля
        LoginHelpers.valid_login_and_valid_password(browser)

        # Клик по кнопке "Войти"
        LoginHelpers.login_button(browser)

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице.')

    @staticmethod
    @pytest.mark.xfail
    def test_phone_tabs(browser):
        """Смена таба выбора аутентификации при вводе телефона в табе 'Почта'"""
        # Открытие сайта
        LoginHelpers.current_url(browser)

        # Явное ожидание таба с текстом "Телефон" и клик по нему
        LoginHelpers.wait_tab_email_button_and_click(browser)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод валидного телефона и валидного пароля
        LoginHelpers.valid_phone_and_valid_password(browser)

        # Клик по кнопке "Войти"
        LoginHelpers.login_button(browser)

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
        # Открытие сайта
        LoginHelpers.current_url(browser)

        # Явное ожидание таба с текстом "Телефон" и клик по нему
        LoginHelpers.wait_tab_email_button_and_click(browser)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод валидного телефона и устаревшего пароля
        LoginHelpers.valid_email_and_not_valid_password(browser)

        # Клик по кнопке "Войти"
        LoginHelpers.login_button(browser)

        # Ожидание текста ошибки входа в ЛК
        LoginHelpers.the_text_of_the_login_error(browser)

        error_message = browser.find_element(*Selectors.FORM_ERROR_MESSAGE)

        assert error_message.text == DataForAssert.ERROR_LOGIN_AND_PASSWORD_TEXT

        print()
        print()
        print(f'Появилась ошибка входа с текстом "{error_message.text}". Так как вход не может быть выполнен '
              f'с предыдущим паролем."')

    @staticmethod
    @pytest.mark.xfail
    def test_email_tabs(browser):
        """Смена таба выбора аутентификации при вводе почты в табе 'Телефон'"""
        # Открытие сайта
        LoginHelpers.current_url(browser)

        # Явное ожидание таба с текстом "Телефон" и клик по нему
        LoginHelpers.wait_tab_phone_button_and_click(browser)

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # Ввод валидного email и пароля
        LoginHelpers.valid_email_and_valid_password(browser)

        # Клик по кнопке "Войти"
        LoginHelpers.login_button(browser)

        # Ожидание текста ошибки входа в ЛК
        LoginHelpers.the_text_of_the_login_error(browser)

        error_message = browser.find_element(*Selectors.FORM_ERROR_MESSAGE)

        assert error_message.text == DataForAssert.ERROR_LOGIN_AND_PASSWORD_TEXT
        print()
        print()
        print(f'Вход в кабинет не выполнен, так как на странице появился текст ошибки "{error_message.text}". '
              f'Смена таба не произошла.')
