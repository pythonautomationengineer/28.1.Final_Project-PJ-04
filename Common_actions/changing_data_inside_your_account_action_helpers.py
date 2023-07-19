from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import link, password, email_valid
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Stability import StabilityTimes


class ChangingDataInsideYourAccount:
    """Необходимые модули, связанные с изменением данных внутри личного кабинета"""

    @staticmethod
    def get_link(browser):
        """Открытие url"""
        browser.get(link)

    @staticmethod
    def wait_email_tab(browser):
        """Явное ожидание таба с текстом "Почта" и клик по нему"""
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        email_button = wait.until(ec.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
        email_button.click()

    @staticmethod
    def valid_email_and_valid_password(browser):
        """Ввод валидного email и пароля"""
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(email_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

    @staticmethod
    def login_button(browser):
        """Клик по кнопке 'Войти'"""
        login_btn = browser.find_element(*Selectors.LOGIN_BUTTON)
        login_btn.click()

    @staticmethod
    def wait_button_changing_full_name(browser):
        """Ожидание кнопки изменения ФИО"""
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC))
