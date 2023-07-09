from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from settings import link, phone_valid, password
from Classes.CSS_Selectors import Selectors


def test_phone_tabs(browser):
    """Смена таба выбора аутентификации при вводе телефона в табе 'Почта'"""
    browser.get(link)

    # Явное ожидание таба с текстом "Почта"
    wait = WebDriverWait(browser, 7)
    email_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_PHONE_BUTTON))
    email_button.click()

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(phone_valid)
    password_input.send_keys(password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    assert browser.find_element(By.CSS_SELECTOR, '#app > main > div > div.home > div.base-card.home__info-card > '
                                                 'h3:nth-child(2)').text == 'Учетные данные'
    print()
    print()
    print('Вход в кабинет выполнен, значит автоматическая смена таба произошла')
