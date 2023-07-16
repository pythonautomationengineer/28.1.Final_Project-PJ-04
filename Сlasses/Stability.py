import platform
import getpass
from selenium.common.exceptions import NoSuchElementException
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
from selenium.webdriver import Keys


class StabilityTimes:
    """Установка времени явного и неявного ожидания для всех тестов"""
    explicit_wait = 10  # Явное ожидание
    implicit_wait = 3  # Неявное ожидание


class Captcha:
    """Функции, связанные с появлением каптчи"""

    @staticmethod
    def handle_captcha(browser):
        """Вызвать AssertionError, если на сайте каптча мешает выполнению теста """
        try:
            captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
            assert not captcha.is_displayed(), DataForAssert.CAPTCHA_INFO
        except NoSuchElementException:
            pass


class OSandUserName:
    """Определение ОС, на которой исполняется код и имени пользователя"""
    apple_os = 'macOS'
    microsoft_os = 'Windows'
    all_support_os = ["Windows", 'macOS']

    @staticmethod
    def os():
        """Операционная система пользователя, запускающего тест"""
        operating_system = platform.system()
        return operating_system

    @staticmethod
    def user_login():
        """Имя пользователя, запускающего тест"""
        username = getpass.getuser()
        return username

    @staticmethod
    def hotkeys(user_os):
        """Задание горячих клавиш для очистки символов в инпутах на разных OS"""
        windows = Keys.CONTROL + "a", Keys.DELETE  # проверено, работает
        apple = Keys.COMMAND + "a", Keys.DELETE  # возможно работает, но проверить не могу, так как нет macOS на руках

        if user_os == OSandUserName.microsoft_os:
            return windows
        elif user_os == OSandUserName.apple_os:
            return apple
