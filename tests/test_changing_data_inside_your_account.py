import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from Common_actions.changing_data_inside_your_account_action_helpers import ChangingDataInsideYourAccount as Cd
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from Сlasses.FakePerson import FakePerson
from Сlasses.Stability import OSandUserName, HotKeys
from Сlasses.Stability import StabilityTimes, Captcha


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
        """Добавление/изменение отчества внутри личного кабинета"""

        # Открытие url
        Cd.get_link(browser)

        # Явное ожидание таба почта
        Cd.wait_email_tab(browser)

        # Проверка наличия/отсутствия каптчи
        Captcha.handle_captcha(browser)

        # Ввод email и пароля
        Cd.valid_email_and_valid_password(browser)

        # Клик по кнопке "Войти"
        Cd.login_button(browser)

        # Явное ожидание кнопки изменения ФИО
        Cd.wait_button_changing_full_name(browser)

        # Изначальное отчество
        start_patronymic_name = browser.find_element(*Selectors.CURRENT_FIRST_NAME_AND_MIDDLE_NAME).text.split()[1]

        # Клик на иконку изменения ФИО
        Cd.button_changing_full_name(browser)

        # Явное ожидание поля с текстом 'Отчество'"
        Cd.user_patronymic_input(browser)

        # Клик по полю отчества
        Cd.click_on_user_patronymic_input(browser)

        # Получение горячих клавиш для конкретной OS пользовательской машины
        os_hotkeys = HotKeys.hotkeys(OSandUserName.os())

        # Удаление старого отчества и ввод нового отчества
        browser.find_element(*Selectors.USER_PATRONYMIC).send_keys(os_hotkeys)
        browser.find_element(*Selectors.USER_PATRONYMIC).send_keys(
            FakePerson.generate_patronymic_name_of_man(start_patronymic_name))

        # Клик по кнопке сохранения ФИО
        Cd.user_full_name_editor_save(browser)

        # Явное ожидание тост-уведомления
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

        # Открытие url
        Cd.get_link(browser)

        # Явное ожидание таба почта
        Cd.wait_email_tab(browser)

        # Проверка наличия/отсутствия каптчи
        Captcha.handle_captcha(browser)

        # Ввод email и пароля
        Cd.valid_email_and_valid_password(browser)

        # Клик по кнопке "Войти"
        Cd.login_button(browser)

        # Явное ожидание кнопки изменения ФИО
        Cd.wait_button_changing_full_name(browser)

        # Текущая фамилия
        start_last_name = browser.find_element(*Selectors.CURRENT_LAST_NAME).text

        # Текущее имя и отчество
        start_first_name_and_middle_name = browser.find_element(*Selectors.CURRENT_FIRST_NAME_AND_MIDDLE_NAME).text

        # Текущее имя
        start_first_name = start_first_name_and_middle_name.split()[0]

        # Клик по кнопке изменения ФИО
        Cd.button_changing_full_name(browser)

        # Явное ожидание поля с текстом 'Фамилия'"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.USER_LASTNAME))

        # Клик по полю фамилии
        Cd.click_on_user_last_name_input(browser)

        # Получение горячих клавиш для конкретной OS пользовательской машины
        os_hotkeys = HotKeys.hotkeys(OSandUserName.os())

        # Очистить поле перед новым вводом фамилии
        browser.find_element(*Selectors.USER_LASTNAME).send_keys(os_hotkeys)

        # Ввод новой фамилии
        browser.find_element(*Selectors.USER_LASTNAME).send_keys(
            FakePerson.generate_last_name_of_man(start_last_name))

        # Клик по полю имени
        Cd.click_on_user_first_name_input(browser)

        # Очистить поле перед новым вводом имени
        browser.find_element(*Selectors.USER_FIRSTNAME).send_keys(os_hotkeys)

        # Ввод нового имени
        browser.find_element(*Selectors.USER_FIRSTNAME).send_keys(
            FakePerson.generate_first_name_of_man(start_first_name))

        # Клик по кнопке сохранения ФИО
        Cd.user_full_name_editor_save(browser)

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

        # Открытие url
        Cd.get_link(browser)

        # Явное ожидание таба почта
        Cd.wait_email_tab(browser)

        # Проверка наличия/отсутствия каптчи
        Captcha.handle_captcha(browser)

        # Ввод email и пароля
        Cd.valid_email_and_valid_password(browser)

        # Клик по кнопке "Войти"
        Cd.login_button(browser)

        # Явное ожидание кнопки изменения ФИО
        Cd.wait_button_changing_full_name(browser)

        # Клик по иконке "карандаш" для смены пароля
        Cd.click_on_changing_password_icon(browser)

        # Явное ожидание поля ввода текущего пароля
        Cd.wait_current_password(browser)

        # Ввод текущего пароля
        Cd.send_current_password(browser)

        # Ввод текущего пароля в поле для нового пароля
        Cd.send_old_password_in_new_password_input(browser)

        # Ввод текущего пароля в поле подтверждения нового пароля
        Cd.send_current_password_in_input_new_confirm_password(browser)

        # Клик по кнопке сохранения пароля
        Cd.click_on_password_save_button(browser)

        # Ожидание текста ошибки
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        wait.until(ec.visibility_of_element_located(Selectors.USER_PASSWORD_EDITOR_ERROR_TEXT))

        # Текст ошибки
        find_text = browser.find_element(*Selectors.USER_PASSWORD_EDITOR_ERROR_TEXT).text

        assert find_text == DataForAssert.PREVIOUSLY_USED_PASSWORD

        print()
        print()
        print(f'Текст "{find_text}" найден на странице, значит текущий пароль изменить на тот же самый нельзя')
