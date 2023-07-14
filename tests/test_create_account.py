import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Сlasses.CSS_Selectors import Selectors
from Сlasses.FakePerson import FakePerson
from settings import link, email_valid, password


# запустить все тесты в этом модуле
#  pytest -k 'create' -v -s
class TestCreateAccount:
    """Позитивные и негативные тесты, связанные с регистрацией"""

    @staticmethod
    @pytest.mark.positive
    def test_registration(browser):
        """Наличие всех необходимых элементов регистрации пользователя на странице"""
        browser.get(link)

        # Явное ожидание ссылки с текстом "Зарегистрироваться"
        wait = WebDriverWait(browser, 7)
        registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

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

        password_input = browser.find_element(*Selectors.REGISTRATION_PASSWORD)
        password_confirm = browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM)

        # Пользовательское соглашение
        user_agreement = browser.find_element(*Selectors.USER_CONCLUSION)

        elements = [h1, reg_p, first_name_form, last_name_form, region, p_data, email_or_phone, password_input,
                    password_confirm, user_agreement]

        for element in elements:
            assert element.is_displayed()

        print()
        print()
        print("Все необходимые элементы на странице присутствуют и были найдены")

    @staticmethod
    @pytest.mark.negative
    def test_invalid_registration(browser):
        """Регистрация по ранее используемым и действующим логином и паролем"""
        browser.get(link)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        wait = WebDriverWait(browser, 7)
        registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        WebDriverWait(browser, 5)
        browser.find_element(*Selectors.USER_CONCLUSION)

        # Имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(""))

        # Фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(""))

        # email или телефон
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание текста 'Учетная запись уже используется'
        WebDriverWait(browser, 5)
        text_information = browser.find_element(*Selectors.TEXT_ACCOUNT_RECORDS_USE_USED)

        assert text_information.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице, значит пользователь с введенными данными уже есть")

    @staticmethod
    @pytest.mark.negative
    def test_return_to_home(browser):
        """Возвращение на главную страницу из модального окна с текстом 'Учетная запись уже используется'"""
        browser.get(link)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        wait = WebDriverWait(browser, 7)
        registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        WebDriverWait(browser, 5)
        browser.find_element(*Selectors.USER_CONCLUSION)

        # Имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(''))

        # Фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(''))

        # email
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание кнопки "Войти" в модальном окне под заголовком 'Учетная запись уже используется'

        WebDriverWait(browser, 5)
        return_button = wait.until(EC.visibility_of_element_located(Selectors.RETURN_BUTTON))

        assert return_button.is_displayed()

        print()
        print()
        print(f"По кнопке 'Войти' в модальном окне под заголовком 'Учетная запись уже используется' можно вернуться на "
              f"главную страницу")
