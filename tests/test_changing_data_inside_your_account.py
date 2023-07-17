import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import link, email_valid, password
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.FakePerson import FakePerson
from Сlasses.Stability import Captcha, OSandUserName, HotKeys
from Сlasses.Stability import StabilityTimes

# запустить все тесты в этом модуле
# pytest -k 'inside' -v -s
class TestChangingDataInsideYourAccountPositive:
    """Позитивные тесты, изменяющие данные пользователя внутри личного кабинета"""

    @staticmethod
    @pytest.mark.xfail
    @pytest.mark.skipif(OSandUserName.os() not in OSandUserName.all_support_os,
                        reason=f'{OSandUserName.user_login()}, '
                               f'тест выполняется только на '
                               f'системах: '
                               f'{", ".join(OSandUserName.all_support_os)},'
                               f' так как'
                               f' используются'
                               f' горячие клавиши'
                               f' данных ОС')
    def test_adding_a_patronymic(browser):
        """Добавление отчества внутри личного кабинета"""
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

        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC))

        # Изначальное отчество
        start_patronymic_name = browser.find_element(*Selectors.CURRENT_FIRST_NAME_AND_MIDDLE_NAME).text.split()[1]

        browser.find_element(*Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC).click()

        # Явное ожидание поля с текстом 'Отчество'"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.USER_PATRONYMIC))

        browser.find_element(*Selectors.USER_PATRONYMIC).click()

        # Получение горячих клавиш для конкретной OS пользовательской машины
        os_hotkeys = HotKeys.hotkeys(OSandUserName.os())

        # Удаление старого отчества и ввод нового отчества
        browser.find_element(*Selectors.USER_PATRONYMIC).send_keys(os_hotkeys)
        browser.find_element(*Selectors.USER_PATRONYMIC).send_keys(
            FakePerson.generate_patronymic_name_of_man(start_patronymic_name))

        # Кнопка сохранения ФИО
        browser.find_element(*Selectors.USER_CONTACTS_EDITOR_SAVE).click()

        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.TEXT_INSIDE_TOAST))

        # Тост-уведомление об изменении ФИО
        toast = browser.find_element(*Selectors.TOAST_CHANGING_NAME_LAST_NAME_PATRONYMIC)
        izm_fio = browser.find_element(*Selectors.TEXT_INSIDE_TOAST).text

        # Новое отчество
        new_patronymic_name = browser.find_element(*Selectors.NEW_FIRST_NAME_AND_PATRONYMIC).text.split()[1]

        assert izm_fio == DataForAssert.TOAST_TEXT and toast.is_displayed()

        print()
        print()
        print(f'Появилось тост-уведомление об успешном изменении отчества. '
              f'Изначальное отчество "{start_patronymic_name}" изменилось на "{new_patronymic_name}".')

    @staticmethod
    @pytest.mark.xfail
    @pytest.mark.skipif(OSandUserName.os() not in OSandUserName.all_support_os,
                        reason=f'{OSandUserName.user_login()}, '
                               f'тест выполняется только на '
                               f'системах: '
                               f'{", ".join(OSandUserName.all_support_os)},'
                               f' так как'
                               f' используются'
                               f' горячие клавиши'
                               f' данных ОС')
    def test_change_of_first_and_last_name(browser):
        """Изменение имени и фамилии внутри личного кабинета"""
        browser.get(link)

        #  Явное ожидание таба с текстом "Почта"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        email_button = wait.until(ec.visibility_of_element_located(Selectors.TAB_EMAIL_BUTTON))
        email_button.click()

        # Если каптча присутствует на странице, то функция handle_captcha выдаст AssertionError,
        # иначе выполнится без ошибок
        Captcha.handle_captcha(browser)

        # email и пароль
        browser.find_element(*Selectors.USERNAME_INPUT).send_keys(email_valid)
        browser.find_element(*Selectors.PASSWORD_INPUT).send_keys(password)

        #  Кнопка "Войти"
        login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
        login_button.click()

        # Ожидание кнопки изменения ФИО
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC))

        # Текущая фамилия
        start_last_name = browser.find_element(*Selectors.CURRENT_LAST_NAME).text

        # Текущее имя и отчество
        start_first_name_and_middle_name = browser.find_element(*Selectors.CURRENT_FIRST_NAME_AND_MIDDLE_NAME).text

        # Текущее имя
        start_first_name = start_first_name_and_middle_name.split()[0]

        # Клик по кнопке изменения ФИО
        browser.find_element(*Selectors.BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC).click()

        # Явное ожидание поля с текстом 'Фамилия'"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.USER_LASTNAME))

        browser.find_element(*Selectors.USER_LASTNAME).click()

        # Получение горячих клавиш для конкретной OS пользовательской машины
        os_hotkeys = HotKeys.hotkeys(OSandUserName.os())

        # Очистить поле перед новым вводом фамилии
        browser.find_element(*Selectors.USER_LASTNAME).send_keys(os_hotkeys)

        # Ввод новой фамилии
        browser.find_element(*Selectors.USER_LASTNAME).send_keys(
            FakePerson.generate_last_name_of_man(start_last_name))

        browser.find_element(*Selectors.USER_FIRSTNAME).click()

        # Очистить поле перед новым вводом имени
        browser.find_element(*Selectors.USER_FIRSTNAME).send_keys(os_hotkeys)

        # Ввод нового имени
        browser.find_element(*Selectors.USER_FIRSTNAME).send_keys(
            FakePerson.generate_first_name_of_man(start_first_name))

        # Сохранение нового ФИО
        browser.find_element(*Selectors.USER_CONTACTS_EDITOR_SAVE).click()

        # Ожидание toast-уведомления об успешном изменении ФИО
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.TEXT_INSIDE_TOAST))

        toast = browser.find_element(*Selectors.TOAST_CHANGING_NAME_LAST_NAME_PATRONYMIC)
        izm_fio = browser.find_element(*Selectors.TEXT_INSIDE_TOAST).text

        # Новое имя
        new_first_name = browser.find_element(*Selectors.NEW_FIRST_NAME_AND_PATRONYMIC).text.split()[0]

        # Новая фамилия
        new_last_name = browser.find_element(*Selectors.NEW_LAST_NAME).text

        assert izm_fio == DataForAssert.TOAST_TEXT and toast.is_displayed()

        print()
        print()
        print(f'Toast-уведомление об изменении данных появилось на странице. Старая фамилия "{start_last_name}"'
              f' была изменена на "{new_last_name}". Старое имя "{start_first_name}"'
              f' было изменено на "{new_first_name}".')


class TestChangingDataInsideYourAccountNegative:
    """Негативные тесты, изменяющие данные пользователя внутри личного кабинета"""

    @staticmethod
    @pytest.mark.xfail
    def test_changing_passwords(browser):
        """Невозможность изменения старого пароля на новый, если он полностью совпадает со старым"""
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

        # Иконка "карандаш" для смены пароля
        browser.find_element(*Selectors.CHANGING_PASSWORD_ICON).click()

        # Явное ожидание поля ввода текущего пароля
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.CURRENT_PASSWORD))

        # Текущий пароль
        browser.find_element(*Selectors.CURRENT_PASSWORD).click()
        browser.find_element(*Selectors.CURRENT_PASSWORD).send_keys(password)

        # Новый пароль
        browser.find_element(*Selectors.NEW_PASSWORD).click()
        browser.find_element(*Selectors.NEW_PASSWORD).send_keys(password)

        # Подтверждение нового пароля
        browser.find_element(*Selectors.CONFIRM_PASSWORD).click()
        browser.find_element(*Selectors.CONFIRM_PASSWORD).send_keys(password)

        # Сохранение нового пароля
        browser.find_element(*Selectors.PASSWORD_SAVE).click()

        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.USER_PASSWORD_EDITOR_ERROR_TEXT))

        # Текст ошибки
        find_text = browser.find_element(*Selectors.USER_PASSWORD_EDITOR_ERROR_TEXT).text

        assert find_text == DataForAssert.PREVIOUSLY_USED_PASSWORD

        print()
        print()
        print(f'Текст "{find_text}" найден на странице, значит текущий пароль изменить на тот же самый нельзя')
