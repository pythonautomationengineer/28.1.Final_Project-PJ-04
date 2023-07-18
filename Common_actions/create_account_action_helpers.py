from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import email_valid
from credentials import link, unused_phone, password
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Characters_generator import CharactersGenerator
from Сlasses.Characters_generator import CharactersGenerator as Cg
from Сlasses.FakePerson import FakePerson
from Сlasses.Stability import Captcha
from Сlasses.Stability import StabilityTimes


class ActionHelpers:

    @staticmethod
    def get_link(browser):
        """Открытие url"""
        browser.get(link)

    @staticmethod
    def registration_explicit_wait(browser):  # ИЗМЕНИТЬ

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        registration = wait.until(ec.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        browser.find_element(*Selectors.USER_CONCLUSION)

    @staticmethod
    def registration_link(browser):
        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        registration = wait.until(ec.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

    @staticmethod
    def registration_button(browser):
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        browser.find_element(*Selectors.USER_CONCLUSION)

    @staticmethod
    def all_registration_elements(browser):
        # Заголовок "Регистрация"
        h1 = browser.find_element(*Selectors.H1_REGISTRATION)

        # Заголовок "Личные данные"
        reg_p = browser.find_element(*Selectors.HEADING_PERSONAL_DATA)

        # Имя
        first_name_form = browser.find_element(*Selectors.FIRST_NAME_INPUT)

        # Фамилия
        last_name_form = browser.find_element(*Selectors.LAST_NAME_INPUT)

        # Регион
        region = browser.find_element(*Selectors.REGION_INPUT)

        # Заголовок "Данные для входа"
        p_data = browser.find_element(*Selectors.HEADER_LOGIN_DETAILS)

        # email
        email_or_phone = browser.find_element(*Selectors.ADDRESS_INPUT)

        # Пароль и подтверждение пароля
        password_input = browser.find_element(*Selectors.REGISTRATION_PASSWORD)
        password_confirm = browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM)

        # Пользовательское соглашение
        user_agreement = browser.find_element(*Selectors.USER_CONCLUSION)

        elements = [h1, reg_p, first_name_form, last_name_form, region, p_data, email_or_phone, password_input,
                    password_confirm, user_agreement]

        for element in elements:
            assert element.is_displayed()

    @staticmethod
    def changing_data_inside_your_account_dry(browser):

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
    def generate_first_name_and_last_name(browser):  # ИЗМЕНИТЬ
        # Сгенерированное имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(""))

        # Сгенерированная фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(""))

    @staticmethod
    def generate_first_name(browser):
        # Сгенерированное имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(''))

    @staticmethod
    def generate_last_name(browser):
        # Сгенерированная фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(""))

    @staticmethod
    def very_long_last_name(browser):
        # Сгенерированная фамилия из 31 символа
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(CharactersGenerator.very_long_last_name_generation())

    @staticmethod
    def one_and_one_symbol_first_and_last_name(browser):
        # Имя из 1 символа
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(CharactersGenerator.one_symbol_generator())

        # Фамилия из 1 символа
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(CharactersGenerator.one_symbol_generator())

    @staticmethod
    def create_account_email_dry(browser):
        # email
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

    @staticmethod
    def create_account_unused_phone_dry(browser):
        # Ввод неиспользуемого телефона
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    @staticmethod
    def valid_password_and_password_confirm(browser):
        # Валидный пароль и подтверждение пароля
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    @staticmethod
    def only_valid_password(browser):
        # Ввод валидного пароля
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)

    @staticmethod
    def eye_icon_password(browser):
        # Клик по иконке "глаз" для изменения атрибута данного элемента
        browser.find_element(*Selectors.EYE_ICON_PASSWORD).click()

    @staticmethod
    def register_button_click(browser):
        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    @staticmethod
    def only_lower_password(browser):
        # Пароли из lower-символов
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
            CharactersGenerator.small_letter_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.small_letter_password_generator())

    @staticmethod
    def latin_password(browser):
        # Ввод паролей не из латинских символов
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
            CharactersGenerator.not_latin_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.not_latin_password_generator())

    @staticmethod
    def dont_match_password(browser):
        # Ввод валидных паролей, но которые не совпадают между собой
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(Cg.dont_match_password_generator_1())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(Cg.dont_match_password_generator_2())
