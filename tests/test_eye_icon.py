from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from settings import link, password


def test_eye_icon_on_password(browser):
    """Элемент <svg>, скрывающий видимость пароля, по клику открывает видимость пароля,
    а при повторном клике скрывает обратно"""
    browser.get(link)

    # Явное ожидание ссылки с текстом "Зарегистрироваться" на главной странице
    wait = WebDriverWait(browser, 7)
    registration = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_THE_TEXT_REGISTER))
    registration.click()

    # Явное ожидание кнопки с текстом "Зарегистрироваться" на странице регистрации
    WebDriverWait(browser, 5)
    browser.find_element(*Selectors.USER_CONCLUSION)

    browser.find_element(*Selectors.REGISTRATION_PASSWORD).send_keys(password)

    attr = browser.find_element(*Selectors.REGISTRATION_PASSWORD_CONFIRM).get_attribute("type")

    # eye_icon
    browser.find_element(*Selectors.EYE_ICON_PASSWORD).click()

    attr_2 = browser.find_element(*Selectors.REGISTRATION_PASSWORD).get_attribute("type")

    assert attr == 'password' and attr_2 == 'text'

    print()
    print()
    print(f"Поле пароля по умолчанию скрывает ввод символами '*',"
          f"а при клике на иконку 'глаз' символы пароля видны пользователю")
