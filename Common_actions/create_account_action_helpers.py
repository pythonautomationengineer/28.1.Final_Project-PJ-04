from Сlasses.Stability import Captcha

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import link, unused_phone, password, email_valid
from Сlasses.CSS_Selectors import Selectors

from Сlasses.FakePerson import FakePerson
from Сlasses.Stability import StabilityTimes


class DuplicateCode:
    @staticmethod
    def registration_explicit_wait(browser):
        browser.get(link)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        registration = wait.until(ec.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        browser.find_element(*Selectors.USER_CONCLUSION)

    @staticmethod
    def changing_data_inside_your_account_dry(browser):
        browser.get(link)

        # Явное ожидание таба с текстом "Почта"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        email_button = wait.until(ec.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
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

        # Ожидание кнопки изменения ФИО
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC))

    @staticmethod
    def generate_first_name_and_last_name(browser):
        # Имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(""))

        # Фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(""))

    @staticmethod
    def create_account_email_dry(browser):
        # email
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

    @staticmethod
    def create_account_unused_phone_dry(browser):
        # Ввод неиспользуемого телефона
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    @staticmethod
    def valid_passwords(browser):
        # Валидный пароль и подтверждение пароля
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
