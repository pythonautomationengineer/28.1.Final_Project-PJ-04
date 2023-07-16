import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from settings import link
from Сlasses.CSS_Selectors import Selectors
from Сlasses.Stability import StabilityTimes


# запустить все тесты в этом модуле
# pytest -k 'other' -v -s

class TestOthers:
    """Тесты, которые не вошли в другие модули"""

    @staticmethod
    @pytest.mark.xfail
    def test_different_links(browser):
        """Отличие ссылок на Пользовательское соглашение и Политику конфиденциальности
        при переходе со страницы авторизации и отличие названий их вкладок в браузере"""
        browser.get(link)

        # Скролл вниз на 100 пикселей
        browser.execute_script("window.scrollBy(0, 100)")

        # Явное ожидание ссылки с текстом "Политикой конфиденциальности"
        wait = WebDriverWait(browser, StabilityTimes.explicit_wait)
        link_1 = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_TEXT_PRIVACY_POLICY))
        link_1.click()

        handles = browser.window_handles

        # Переключение на новую вкладку
        new_tab_handle = handles[-1]
        browser.switch_to.window(new_tab_handle)

        # Заголовок вкладки
        title_text = browser.title

        # Текущий url
        current_url = browser.current_url

        browser.implicitly_wait(StabilityTimes.implicit_wait)

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

        # Заголовок вкладки
        title_text_2 = browser.title

        # Текущий url
        current_url_2 = browser.current_url

        # Неявное ожидание
        browser.implicitly_wait(3)

        # Заголовок статьи пользовательского соглашения
        find_text_h1_2 = browser.find_element(*Selectors.HEADING_ARTICLES_USER_REFERENCES).text

        assert (title_text == title_text_2) and (current_url == current_url_2) and (find_text_h1 == find_text_h1_2)

        print()
        print()
        print('Ссылки на страницы о политике конфиденциальности и пользовательское соглашение ведут на'
              ' одну и ту же страницу, так как у обеих страниц один и тот же url, '
              'заголовок вкладки, заголовок страницы')
