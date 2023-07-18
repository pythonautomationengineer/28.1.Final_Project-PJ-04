from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import link
from credentials import phone_valid, password, email_valid, login, old_password
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Stability import StabilityTimes


class LoginHelpers:
    @staticmethod
    def current_url(browser):
        """Открытие сайта"""
        browser.get(link)

    @staticmethod
    def login_button(browser):
        # Клик по кнопке "Войти"
        browser.find_element(*Selectors.LOGIN_BUTTON).click()

    @staticmethod
    def valid_phone_and_valid_password(browser):
        # Ввод валидного телефона и валидного пароля
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(phone_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

    @staticmethod
    def valid_email_and_valid_password(browser):
        # Ввод валидного email и пароля
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(email_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

    @staticmethod
    def valid_email_and_not_valid_password(browser):
        # Ввод валидного телефона и устаревшего пароля
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(phone_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(old_password)

    @staticmethod
    def valid_login_and_valid_password(browser):
        # Ввод валидного логина и пароля
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(login)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

    @staticmethod
    def wait_tab_phone_button_and_click(browser):
        # Явное ожидание таба с текстом "Телефон" и клик по нему
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        phone_button = wait.until(ec.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
        phone_button.click()

    @staticmethod
    def wait_tab_email_button_and_click(browser):
        # Явное ожидание таба с текстом "Почта" и клик по нему
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        email_button = wait.until(ec.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
        email_button.click()

    @staticmethod
    def wait_tab_login_button_and_click(browser):
        # Явное ожидание таба с текстом "Логин" и клик по нему
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        login_button = wait.until(ec.visibility_of_element_located(Selectors.TAB_LOGIN_LOGIN))
        login_button.click()

    @staticmethod
    def the_text_of_the_login_error(browser):
        # Ожидание текста ошибки входа в ЛК
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.FORM_ERROR_MESSAGE))
