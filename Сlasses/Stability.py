from selenium.common.exceptions import NoSuchElementException
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Data_for_Assert import DataForAssert
import platform
import getpass


class StabilityTimes:
    """Установка времени явного и неявного ожидания"""
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


class OperationSystemAndUserName:
    """Определение ОС, на которой исполняется код и имени пользователя"""
    @staticmethod
    def os():
        """Операционная система"""
        operating_system = platform.system()
        return operating_system

    @staticmethod
    def user():
        """Имя пользователя"""
        username = getpass.getuser()
        return username
