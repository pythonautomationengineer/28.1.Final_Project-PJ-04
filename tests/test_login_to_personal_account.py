import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.try_except_exception import handle_captcha
from settings import link, login, password, email_valid, phone_valid


# запустить все тесты в этом модуле
# pytest -k 'personal' -v -s

class TestLogin:
    """Позитивные и негативные тесты, которые проверяют вход в личный кабинет"""

    @staticmethod
    @pytest.mark.positive
    def test_login(browser):
        """Вход в личный кабинет по валидному телефону и паролю"""
        browser.get(link)

        # Явное ожидание таба с текстом "Телефон"
        wait = WebDriverWait(browser, 7)
        phone_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
        phone_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без
        # ошибок
        handle_captcha(browser)

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
    @pytest.mark.positive
    def test_login_2(browser):
        """Вход в личный кабинет по валидному email и паролю"""
        browser.get(link)

        # Явное ожидание таба с текстом "Почта"
        wait = WebDriverWait(browser, 7)
        email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
        email_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без
        # ошибок
        handle_captcha(browser)

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
    @pytest.mark.positive
    def test_login_3(browser):
        """Вход в личный кабинет по валидному логину и паролю"""
        browser.get(link)

        # Явное ожидание таба с текстом "Логин"
        wait = WebDriverWait(browser, 7)
        login_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_LOGIN_LOGIN))
        login_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError, иначе выполнится без
        # ошибок
        handle_captcha(browser)

        # Логин и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(login)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

        # Кнопка "Войти"
        browser.find_element(*Selectors.LOGIN_BUTTON).click()

        assert browser.find_element(*Selectors.CREDENTIALS).text == DataForAssert.CREDENTIALS

        print()
        print()
        print(f'Вход успешно выполнен. Текст "{DataForAssert.CREDENTIALS}" найден на странице.')
