from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from settings import link, login, password
from Classes.CSS_Selectors import Selectors


def test_login(browser):
    """Вход в личный кабинет по валидному логину и паролю"""
    browser.get(link)

    # Явное ожидание таба с текстом "Логин"
    wait = WebDriverWait(browser, 7)
    login_button = wait.until(EC.visibility_of_element_located(Selectors.TAB_LOGIN_LOGIN))
    login_button.click()

    try:
        captcha = browser.find_element(*Selectors.CAPTCHA_TEXT)
        assert not captcha.is_displayed(), 'Каптча на сайте! Придется разок войти руками в ЛК, а после запустить тест'
    except NoSuchElementException:
        pass

    username_input = browser.find_element(*Selectors.USERNAME_INPUT)
    password_input = browser.find_element(*Selectors.PASSWORD_INPUT)

    username_input.send_keys(login)
    password_input.send_keys(password)

    login_button = browser.find_element(*Selectors.LOGIN_BUTTON)
    login_button.click()

    assert browser.find_element(By.CSS_SELECTOR, '#app > main > div > div.home > div.base-card.home__info-card > '
                                                 'h3:nth-child(2)').text == 'Учетные данные'

    print()
    print()
    print('Вход успешно выполнен')
