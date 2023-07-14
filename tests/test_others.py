import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Сlasses.CSS_Selectors import Selectors
from settings import link, password
from Сlasses.Data_for_Assert import DataForAssert


# запустить все тесты в этом модуле
# pytest -k 'other' -v -s

class TestOthers:
    """Тесты, которые не вошли в другие модули"""

    @staticmethod
    def test_different_links(browser):
        """Отличие ссылок на Пользовательское соглашение и Политику конфиденциальности
        при переходе со страницы авторизации и отличие названий их вкладок в браузере"""
        browser.get(link)

        # Скролл вниз на 100 пикселей
        browser.execute_script("window.scrollBy(0, 100)")

        # Явное ожидание ссылки с текстом "Политикой конфиденциальности"
        wait = WebDriverWait(browser, 30)
        link_1 = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_TEXT_PRIVACY_POLICY))
        link_1.click()

        handles = browser.window_handles

        # Переключение на новую вкладку
        new_tab_handle = handles[-1]
        browser.switch_to.window(new_tab_handle)

        title_text = browser.title
        current_url = browser.current_url

        browser.implicitly_wait(3)

        # Заголовок статьи политики конфиденциальности
        find_text_h1 = browser.find_element(*Selectors.HEADING_STATE_POLITICS_PRIVACY_POLICY).text

        browser.get(link)

        # Скролл вниз на 100 пикселей
        browser.execute_script("window.scrollBy(0, 100)")

        # Явное ожидание ссылки с текстом "Пользовательским соглашением"
        wait = WebDriverWait(browser, 6)
        link_1 = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_TEXT_USER_AGREEMENT))
        link_1.click()

        handles = browser.window_handles

        # Переключение на новую вкладку
        new_tab_handle = handles[-1]
        browser.switch_to.window(new_tab_handle)

        title_text_2 = browser.title
        current_url_2 = browser.current_url

        browser.implicitly_wait(3)

        # Заголовок статьи пользовательского соглашения
        find_text_h1_2 = browser.find_element(*Selectors.HEADING_ARTICLES_USER_REFERENCES).text

        assert (title_text == title_text_2) and (current_url == current_url_2) and (find_text_h1 == find_text_h1_2)

        print()
        print()
        print('Ссылки на страницы о политике конфиденциальности и пользовательское соглашение ведут на'
              ' одну и ту же страницу, так как у обеих страниц один и тот же url, '
              'заголовок вкладки, заголовок страницы')

    @staticmethod
    @pytest.mark.positive
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

        assert attr == DataForAssert.PASSWORD_ICON_ATTRIBUTE_1 and attr_2 == DataForAssert.PASSWORD_ICON_ATTRIBUTE_2

        print()
        print()
        print(f"Поле пароля по умолчанию скрывает ввод символами '*', "
              f"а при клике на иконку 'глаз' символы пароля видны пользователю")
