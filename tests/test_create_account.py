import pytest

from Сlasses.Characters_generator import CharactersGenerator

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.FakePerson import FakePerson
from Сlasses.Characters_generator import CharactersGenerator as Cg
from settings import link, unused_phone, password, email_valid


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

    @staticmethod
    @pytest.mark.positive
    def test_valid_registration(browser):
        """Отправка сайтом кода подтверждения регистрации при всех введенных валидных данных, которые ранее
        не были использованы"""
        browser.get(link)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        wait = WebDriverWait(browser, 5)
        registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
        registration.click()

        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        WebDriverWait(browser, 5)
        browser.find_element(*Selectors.USER_CONCLUSION)

        # Имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(FakePerson.generate_first_name_of_man(''))

        # Фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(''))

        # Номер
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)

        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание текста о том, что код подтверждения телефона был отправлен по указанному номеру
        WebDriverWait(browser, 5)
        text_information = browser.find_element(*Selectors.CONFIRMATION_PHONE_TEXT)

        assert text_information.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице, значит пользователю "
              f"код подтверждения телефона был отправлен")

    @staticmethod
    @pytest.mark.negative
    def test_short_password(browser):
        """Появление сообщения в форме регистрации с текстом "Длина пароля должна быть не менее 8 символов"
        под полем "Новый пароль" при вводе пароля из 7 символов"""
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

        # Телефон
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

        # Пароли
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(CharactersGenerator.short_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.short_password_generator())

        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание текста "Длина пароля должна быть не менее 8 символов" под полем 'Пароль'"
        WebDriverWait(browser, 3)
        text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        # Явное ожидание текста "Длина пароля должна быть не менее 8 символов" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, 3)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information.text == DataForAssert.VERY_SHORT_PASSWORD \
               and text_information_2.text == DataForAssert.VERY_SHORT_PASSWORD

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке "
              f"'Зарегистрироваться'. Значит валидация на короткое значение пароля работает")

    @staticmethod
    @pytest.mark.negative
    def test_big_letter(browser):
        """Появление сообщения в форме регистрации с текстом "Пароль должен содержать хотя бы одну заглавную букву"
        под полем "Пароль" и "Подтверждение пароля" при введении 8 символов: маленьких букв и цифр"""
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

        # Телефон
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

        # Пароли
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
            CharactersGenerator.small_letter_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.small_letter_password_generator())

        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание текста Пароль должен содержать хотя бы одну заглавную букву" под полем 'Пароль'"
        WebDriverWait(browser, 2)
        text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD)

        # Явное ожидание текста "Пароль должен содержать хотя бы одну заглавную букву" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, 2)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information.text == DataForAssert.BIG_LETTER_TEXT_IN_PASSWORD \
               and text_information_2.text == DataForAssert.BIG_LETTER_TEXT_IN_PASSWORD

        print()
        print()
        print(
            f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке "
            f"'Зарегистрироваться'. Значит валидация на заглавную букву пароля работает")

    @staticmethod
    @pytest.mark.negarive
    def test_latin_password(browser):
        """Появление сообщения в форме регистрации с текстом "Пароль должен содержать только латинские буквы" под полем
        "Пароль" и "Подтверждение пароля при введении 9 символов кириллицы"""
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

        # Телефон
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

        # Пароли
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(
            CharactersGenerator.not_latin_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.not_latin_password_generator())

        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание текста "Пароль должен содержать только латинские буквы" под полем 'Пароль'"
        WebDriverWait(browser, 2)
        text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD)

        # Явное ожидание текста "Пароль должен содержать только латинские буквы" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, 2)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information.text == DataForAssert.ONLY_LATIN_LETTER_TEXT_IN_PASSWORD \
               and text_information_2.text == DataForAssert.ONLY_LATIN_LETTER_TEXT_IN_PASSWORD

        print()
        print()
        print(
            f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке "
            f"'Зарегистрироваться'. Значит валидация на латинские символы пароля работает.")

    @staticmethod
    @pytest.mark.negarive
    def test_pass_dont_match(browser):
        """Выводится "Пароли не совпадают" под полем "Подтверждение пароля", если пользователь ввел разные пароли
        при регистрации"""
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

        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(unused_phone)

        # Пароли
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(Cg.p_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(Cg.p2_password_generator())

        # Кнопка "Зарегистрироваться"
        browser.find_element(*Selectors.THE_REGISTER_BUTTON).click()

        # Явное ожидание текста "Пароли не совпадают" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, 2)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information_2.text == DataForAssert.PASSWORDS_DO_NOT_MATCH

        print()
        print()
        print(f"Текст '{text_information_2.text}' найден на странице под полем 'Подтверждение пароля' после клика "
              f"по кнопке 'Зарегистрироваться'. Значит валидация на подтверждение пароля работает")
