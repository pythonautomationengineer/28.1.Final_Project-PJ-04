from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import email_valid
from credentials import link, unused_phone, password
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Characters_generator import CharactersGenerator
from Сlasses.Characters_generator import CharactersGenerator as Cg
from Сlasses.FakePerson import FakePerson
from Сlasses.Stability import StabilityTimes


class ActionHelpers:
    """Необходимые методы, связанные с созданием аккаунта"""
    @staticmethod
    def get_link(browser):
        """Открытие url"""
        browser.get(link)

    @staticmethod
    def registration_link(browser):
        """Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице"""
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        registration = wait.until(ec.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

    @staticmethod
    def registration_button(browser):
        """Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации"""
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        browser.find_element(*Selectors.USER_CONCLUSION)

    @staticmethod
    def generate_first_name(browser):
        """Генерация и ввод валидного имени"""
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(''))

    @staticmethod
    def generate_last_name(browser):
        """Генерация и ввод валидной фамилии"""
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(""))

    @staticmethod
    def very_long_last_name(browser):
        """Генерация и ввод фамилии из 31 символа"""
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(CharactersGenerator.very_long_last_name_generation())

    @staticmethod
    def very_long_first_name(browser):
        """Генерация и ввод имени из 31 символа"""
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(
            CharactersGenerator.very_long_first_name_generation())

    @staticmethod
    def one_and_one_symbol_first_and_last_name(browser):
        """Генерация и ввод имени и фамилии из 1 символа"""
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(CharactersGenerator.one_symbol_generator())
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(CharactersGenerator.one_symbol_generator())

    @staticmethod
    def create_account_email_dry(browser):
        """Ввод валидного email"""
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

    @staticmethod
    def create_account_unused_phone_dry(browser):
        """Ввод неиспользованного телефона"""
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

    @staticmethod
    def valid_password_and_password_confirm(browser):
        """Генерация и ввод валидного пароля и подтверждение пароля"""
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

    @staticmethod
    def only_valid_password(browser):
        """Ввод валидного пароля от учетной записи"""
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)

    @staticmethod
    def eye_icon_password(browser):
        """Клик по иконке "глаз" для изменения атрибута данного элемента"""
        browser.find_element(*Selectors.EYE_ICON_PASSWORD).click()

    @staticmethod
    def register_button_click(browser):
        """Клик по кнопке "Зарегистрироваться"""
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

    @staticmethod
    def only_lower_password(browser):
        """Генерация и ввод пароля и подтверждение пароля из lower-символов"""
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
            CharactersGenerator.small_letter_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.small_letter_password_generator())

    @staticmethod
    def latin_password(browser):
        """Генерация и ввод паролей не из латинских символов"""
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
            CharactersGenerator.not_latin_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.not_latin_password_generator())

    @staticmethod
    def dont_match_password(browser):
        """Генерация и ввод валидных паролей, но которые не совпадают между собой"""
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(Cg.dont_match_password_generator_1())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(Cg.dont_match_password_generator_2())

    @staticmethod
    def very_short_passwords(browser):
        """Генерация и ввод паролей короче необходимых"""
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(CharactersGenerator.short_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.short_password_generator())
