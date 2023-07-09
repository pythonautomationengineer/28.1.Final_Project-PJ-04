from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from settings import link


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

    password = browser.find_element(*Selectors.REGISTRATION_PASSWORD)
    password_confirm = browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM)

    # Пользовательское соглашение
    user_agreement = browser.find_element(*Selectors.USER_CONCLUSION)

    elements = [h1, reg_p, first_name_form, last_name_form, region, p_data, email_or_phone, password, password_confirm,
                user_agreement]

    for element in elements:
        assert element.is_displayed()

    print()
    print()
    print("Все элементы на странице присутствуют и были найдены")
