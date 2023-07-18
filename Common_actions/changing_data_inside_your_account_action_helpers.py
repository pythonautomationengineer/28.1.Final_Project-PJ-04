
from Сlasses.Stability import Captcha

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from credentials import link, unused_phone, password, email_valid
from Сlasses.CSS_Selectors import Selectors

from Сlasses.Stability import StabilityTimes


def get_link(browser):
    """Открытие url"""
    browser.get(link)


def changing_data_inside_your_account_dry(browser):
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