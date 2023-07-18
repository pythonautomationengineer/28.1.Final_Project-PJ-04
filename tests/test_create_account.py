from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Common_actions.create_account_action_helpers import ActionHelpers
from credentials import email_valid
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Characters_generator import CharactersGenerator
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.FakePerson import FakePerson
from Сlasses.Stability import StabilityTimes


class TestCreateAccountNegative:
    """Негативные тесты, связанные с регистрацией"""

    @staticmethod
    def test_invalid_registration(browser):
        """Регистрация по ранее используемым и действующим логином и паролем"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # Ввод валидного email
        ActionHelpers.create_account_email_dry(browser)

        # Валидный пароль и подтверждение пароля
        ActionHelpers.valid_password_and_password_confirm(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста 'Учетная запись уже используется'
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.TEXT_ACCOUNT_RECORDS_USE_USED)

        assert text_information.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице, значит пользователь с введенными данными уже есть")

    @staticmethod
    def test_returning_to_the_home_page(browser):
        """Возвращение на главную страницу из модального окна с текстом 'Учетная запись уже используется'"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # email
        browser.find_element(*Selectors.ADDRESS_INPUT).send_keys(email_valid)

        # Валидный пароль и подтверждение пароля
        ActionHelpers.valid_password_and_password_confirm(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание кнопки "Войти" в модальном окне под заголовком 'Учетная запись уже используется'
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        return_button = wait.until(ec.visibility_of_element_located(Selectors.RETURN_BUTTON))

        # Клик по кнопе возврата на страницу регистрации
        return_button.click()

        # Явное ожидание заголовка с текстом "Авторизация"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        h1 = wait.until(ec.visibility_of_element_located(Selectors.H1_REGISTRATION))

        assert h1.is_displayed()

        print()
        print()
        print(f"По кнопке 'Войти' в модальном окне можно вернуться на главную страницу")

    @staticmethod
    def test_short_password(browser):
        """Появление сообщения в форме регистрации с текстом "Длина пароля должна быть не менее 8 символов"
        под полем "Новый пароль" при вводе пароля из 7 символов"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # Ввод невалидного телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Ввод паролей короче необходимых
        browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(CharactersGenerator.short_password_generator())
        browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).send_keys(
            CharactersGenerator.short_password_generator())

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста "Длина пароля должна быть не менее 8 символов" под полем 'Пароль'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        # Явное ожидание текста "Длина пароля должна быть не менее 8 символов" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information.text == DataForAssert.VERY_SHORT_PASSWORD \
               and text_information_2.text == DataForAssert.VERY_SHORT_PASSWORD

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке "
              f"'Зарегистрироваться'. Значит валидация на короткое значение пароля работает")

    @staticmethod
    def test_big_letter(browser):
        """Появление сообщения в форме регистрации с текстом "Пароль должен содержать хотя бы одну заглавную букву"
        под полем "Пароль" и "Подтверждение пароля" при введении 8 символов: маленьких букв и цифр"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # Ввод невалидного телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Пароли из lower-символов
        ActionHelpers.only_lower_password(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста Пароль должен содержать хотя бы одну заглавную букву" под полем 'Пароль'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD)

        # Явное ожидание текста "Пароль должен содержать хотя бы одну заглавную букву" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information.text == DataForAssert.BIG_LETTER_TEXT_IN_PASSWORD \
               and text_information_2.text == DataForAssert.BIG_LETTER_TEXT_IN_PASSWORD

        print()
        print()
        print(
            f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке "
            f"'Зарегистрироваться'. Значит валидация на заглавную букву пароля работает")

    @staticmethod
    def test_latin_password(browser):
        """Появление сообщения в форме регистрации с текстом "Пароль должен содержать только латинские буквы" под полем
        "Пароль" и "Подтверждение пароля при введении 9 символов кириллицы"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # Ввод невалидного телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Ввод паролей не из латинских символов
        ActionHelpers.latin_password(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста "Пароль должен содержать только латинские буквы" под полем 'Пароль'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD)

        # Явное ожидание текста "Пароль должен содержать только латинские буквы" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information.text == DataForAssert.ONLY_LATIN_LETTER_TEXT_IN_PASSWORD \
               and text_information_2.text == DataForAssert.ONLY_LATIN_LETTER_TEXT_IN_PASSWORD

        print()
        print()
        print(
            f"Текст '{text_information.text}' найден на странице в 2 местах после клика по кнопке "
            f"'Зарегистрироваться'. Значит валидация на латинские символы пароля работает.")

    @staticmethod
    def test_pass_dont_match(browser):
        """Выводится "Пароли не совпадают" под полем "Подтверждение пароля", если пользователь ввел разные пароли
        при регистрации"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # Ввод невалидного телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Ввод валидных паролей, но которые не совпадают между собой
        ActionHelpers.dont_match_password(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста "Пароли не совпадают" под полем 'Подтверждение пароля'"
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information_2 = browser.find_element(*Selectors.TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION)

        assert text_information_2.text == DataForAssert.PASSWORDS_DO_NOT_MATCH

        print()
        print()
        print(f"Текст '{text_information_2.text}' найден на странице под полем 'Подтверждение пароля' после клика "
              f"по кнопке 'Зарегистрироваться'. Значит валидация на подтверждение пароля работает")

    @staticmethod
    def test_not_valid_registration(browser):
        """Регистрация со всеми валидными полями кроме имени (слишком длинное имя)"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Имя
        browser.find_element(*Selectors.FIRST_NAME_INPUT).send_keys(
            CharactersGenerator.very_long_first_name_generation())

        # Фамилия
        browser.find_element(*Selectors.LAST_NAME_INPUT).send_keys(FakePerson.generate_last_name_of_man(''))

        # Ввод неиспользуемого телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Валидный пароль и подтверждение пароля
        ActionHelpers.valid_password_and_password_confirm(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста о том, что валидная длина имени от 2 до 30 символов
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.FIRST_NAME_ERROR_TEXT)

        assert text_information.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице, значит при регистрации "
              f"было введено слишком длинное имя, так как имя было введено полностью кириллическое")

    @staticmethod
    def test_valid_registration(browser):
        """Регистрация со всеми валидными полями кроме фамилии (слишком длинная фамилия)"""
        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Сгенерированное имя
        ActionHelpers.generate_first_name(browser)

        # Сгенерированная фамилия из 31 символа
        ActionHelpers.very_long_last_name(browser)

        # Ввод неиспользуемого телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Валидный пароль и подтверждение пароля
        ActionHelpers.valid_password_and_password_confirm(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста о том, что валидная длина фамилии от 2 до 30 символов
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.LAST_NAME_ERROR_TEXT)

        assert text_information.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице, значит при регистрации "
              f"была введена слишком длинная фамилия, так как фамилия была введена полностью кириллическая")

    @staticmethod
    def test_valid_registration_too(browser):
        """Регистрация со всеми валидными полями кроме фамилии и имени (слишком короткая фамилия и имя)"""
        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени и фамилии из 1 символа
        ActionHelpers.one_and_one_symbol_first_and_last_name(browser)

        # Ввод неиспользуемого телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Валидный пароль и подтверждение пароля
        ActionHelpers.valid_password_and_password_confirm(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста о том, что валидная длина фамилии от 2 до 30 символов
        WebDriverWait(browser, StabilityTimes.explicit_wait)

        # Текст ошибки под полем с фамилией
        text_information = browser.find_element(*Selectors.LAST_NAME_ERROR_TEXT)

        # Текст ошибки под полем имени
        text_information_2 = browser.find_element(*Selectors.FIRST_NAME_ERROR_TEXT)

        assert text_information.is_displayed() and text_information_2.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице в 2 местах, "
              f"значит при регистрации была введена слишком короткая фамилия и слишком короткое имя")


class TestCreateAccountPositive:
    """Позитивные тесты, связанные с регистрацией"""

    @staticmethod
    def test_registration(browser):
        """Наличие всех необходимых элементов регистрации пользователя на странице"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться"
        ActionHelpers.registration_link(browser)

        # Все необходимые поля и ссылки страницы регистрации
        ActionHelpers.all_registration_elements(browser)

        print()
        print()
        print("Все необходимые элементы на странице присутствуют и были найдены")

    @staticmethod
    def test_valid_registration(browser):
        """Отправка сайтом кода подтверждения регистрации при всех введенных валидных данных, которые ранее
        не были использованы"""

        # Открытие url
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод имени
        # Ввод фамилии
        ActionHelpers.generate_first_name_and_last_name(browser)

        # Ввод невалидного телефона
        ActionHelpers.create_account_unused_phone_dry(browser)

        # Валидный пароль и подтверждение пароля
        ActionHelpers.valid_password_and_password_confirm(browser)

        # Кнопка "Зарегистрироваться"
        ActionHelpers.register_button_click(browser)

        # Явное ожидание текста о том, что код подтверждения телефона был отправлен по указанному номеру
        WebDriverWait(browser, StabilityTimes.explicit_wait)
        text_information = browser.find_element(*Selectors.CONFIRMATION_PHONE_TEXT)

        assert text_information.is_displayed()

        print()
        print()
        print(f"Текст '{text_information.text}' найден на странице, значит пользователю "
              f"код подтверждения телефона был отправлен")

    @staticmethod
    def test_eye_icon_on_password(browser):
        """Элемент <svg>, скрывающий видимость пароля, по клику открывает видимость пароля,
        а при повторном клике скрывает обратно"""

        # Открытие URL
        ActionHelpers.get_link(browser)

        # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
        ActionHelpers.registration_link(browser)
        # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
        ActionHelpers.registration_button(browser)

        # Ввод валидного пароля
        ActionHelpers.only_valid_password(browser)

        # Изначальный атрибут элемента скрытия/открытия пароля
        start_attr = browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).get_attribute("type")

        # Клик по иконке "глаз" для изменения атрибута данного элемента
        ActionHelpers.eye_icon_password(browser)

        # Атрибут элемента скрытия/открытия пароля после клика
        end_attr = browser.find_element(*Selectors.REGISTRATION_PASSWORD).get_attribute("type")

        assert start_attr == DataForAssert.PASSWORD_ICON_ATTRIBUTE_1 \
               and end_attr == DataForAssert.PASSWORD_ICON_ATTRIBUTE_2

        print()
        print()
        print(f"Поле пароля по умолчанию скрывает ввод символами '*', "
              f"а при клике на иконку 'глаз' символы пароля видны пользователю")
