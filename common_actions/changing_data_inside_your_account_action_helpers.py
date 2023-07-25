from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from credentials import link, password, email_valid
from classes.css_selectors import Selectors
from classes.stability import StabilityTimes


class ChangingDataInsideYourAccount:
    """Необходимые методы, связанные с изменением данных внутри личного кабинета"""

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

    @staticmethod
    def button_changing_full_name(browser):
        """Клик на иконку изменения ФИО"""
        browser.find_element(*Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC).click()

    @staticmethod
    def user_patronymic_input(browser):
        """Явное ожидание поля с текстом 'Отчество'"""
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.USER_PATRONYMIC))

    @staticmethod
    def click_on_user_patronymic_input(browser):
        """Клик по полю отчества"""
        browser.find_element(*Selectors.USER_PATRONYMIC).click()

    @staticmethod
    def user_full_name_editor_save(browser):
        """Клик по кнопке сохранения ФИО"""
        browser.find_element(*Selectors.USER_CONTACTS_EDITOR_SAVE).click()

    @staticmethod
    def click_on_user_last_name_input(browser):
        """Клик по полю фамилии"""
        browser.find_element(*Selectors.USER_LASTNAME).click()

    @staticmethod
    def click_on_user_first_name_input(browser):
        """Клик по полю имени"""
        browser.find_element(*Selectors.USER_FIRSTNAME).click()

    @staticmethod
    def click_on_changing_password_icon(browser):
        """Клик по иконке 'карандаш' для смены пароля"""
        browser.find_element(*Selectors.CHANGING_PASSWORD_ICON).click()

    @staticmethod
    def wait_current_password(browser):
        """Явное ожидание поля ввода текущего пароля"""
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.CURRENT_PASSWORD))

    @staticmethod
    def send_current_password(browser):
        """Ввод текущего пароля"""
        browser.find_element(*Selectors.CURRENT_PASSWORD).click()
        browser.find_element(*Selectors.CURRENT_PASSWORD).send_keys(password)

    @staticmethod
    def send_old_password_in_new_password_input(browser):
        """Ввод текущего пароля в поле для нового пароля"""
        browser.find_element(*Selectors.NEW_PASSWORD).click()
        browser.find_element(*Selectors.NEW_PASSWORD).send_keys(password)

    @staticmethod
    def send_current_password_in_input_new_confirm_password(browser):
        """Ввод текущего пароля в поле подтверждения нового пароля"""
        browser.find_element(*Selectors.CONFIRM_PASSWORD).click()
        browser.find_element(*Selectors.CONFIRM_PASSWORD).send_keys(password)

    @staticmethod
    def click_on_password_save_button(browser):
        """Клик по кнопке сохранения пароля"""
        browser.find_element(*Selectors.PASSWORD_SAVE).click()
