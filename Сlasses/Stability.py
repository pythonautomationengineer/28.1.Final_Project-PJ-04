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
    all_support_os = ["Windows", 'macOS', 'Linux']
    apple_os = 'macOS'
    microsoft_os = 'Windows'
    linux = 'Linux'

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
        win = Keys.CONTROL + "a", Keys.DELETE
        apple = Keys.COMMAND + "a", Keys.DELETE
        linux = Keys.CONTROL + "a", Keys.DELETE
        if user_os == OSandUserName.microsoft_os:
            return win
        elif user_os == OSandUserName.apple_os:
            return apple
        elif user_os == OSandUserName.linux:
            return linux
