from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Classes.CSS_Selectors import Selectors
from settings import link


class TestDifferentLinks:
    def test_dif_links(self, browser):
        """Отличие ссылок на Пользовательское соглашение и Политику конфиденциальности
        при переходе со страницы авторизации и отличие названий их вкладок в браузере"""
        browser.get(link)

        # Скролл вниз на 100 пикселей на всякий случай
        browser.execute_script("window.scrollBy(0, 100)")

        # Явное ожидание ссылки с текстом "Политикой конфиденциальности"
        wait = WebDriverWait(browser, 6)
        link_1 = wait.until(EC.visibility_of_element_located(Selectors.LINK_WITH_TEXT_PRIVACY_POLICY))
        link_1.click()

        handles = browser.window_handles

        # переключение на новую вкладку
        new_tab_handle = handles[-1]
        browser.switch_to.window(new_tab_handle)

        title_text = browser.title
        corrent_url = browser.current_url

        browser.implicitly_wait(3)
        # Заголовок статьи политики конфиденциальности
        find_text_h1 = browser.find_element(*Selectors.HEADING_STATE_POLITICS_PRIVACY_POLICY).text

        browser.get(link)

        # Скролл вниз на 100 пикселей на всякий случай
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
        corrent_url_2 = browser.current_url

        browser.implicitly_wait(3)
        # Заголовок статьи пользовательского соглашения
        find_text_h1_2 = browser.find_element(*Selectors.HEADING_ARTICLES_USER_REFERENCES).text

        assert title_text == title_text_2 and corrent_url == corrent_url_2 and find_text_h1 == find_text_h1_2

        print()
        print()
        print('Ссылки на страницы о политике конфиденциальности и пользовательское соглашение ведут на'
              ' одну и ту же страницу, так как у обеих страниц один и тот же url, '
              'заголовок вкладки, заголовок страницы ')
