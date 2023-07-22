from selenium.webdriver.common.by import By


class Selectors:
    """CSS селекторы для тестов"""

    # Текст при не вводе каптчи
    CAPTCHA_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > div > form > div.rt-captcha.login-form__captcha > '
                                     'div.rt-input-container.rt-captcha__input > span')

    # Табы на главной странице тестируемого сайта
    TAB_EMAIL_BUTTON = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN_LOGIN = (By.ID, 't-btn-tab-login')
    TAB_PHONE_BUTTON = (By.ID, 't-btn-tab-phone')

    # Логин и пароль при авторизации
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.ID, 'kc-login')

    # Cсылка с текстом "Зарегистрироваться" на главной странице
    LINK_WITH_THE_TEXT_REGISTER = (By.ID, 'kc-register')

    # Заголовок H1 "Регистрация"
    H1_REGISTRATION = (By.CSS_SELECTOR, '#page-right > div > div > h1')

    # Заголовок "Личные данные"
    HEADING_PERSONAL_DATA = (By.CSS_SELECTOR, '#page-right > div > div > div > form > p:nth-child(1)')

    # Поля "Имя" при регистрации
    FIRST_NAME_INPUT = (By.CSS_SELECTOR,
                        '#page-right > div > div > div > form > div.name-container > div:nth-child('
                        '1) >'
                        'div > input')

    # Поля "Фамилия" при регистрации
    LAST_NAME_INPUT = (By.CSS_SELECTOR,
                       '#page-right > div > div > div > form > div.name-container > div:nth-child('
                       '2) > div > input')

    # Поля "Регион" при регистрации
    REGION_INPUT = (By.CSS_SELECTOR,
                    '#page-right > div > div > div > form > '
                    'div.rt-select.rt-select--search.register-form__dropdown > div > div > input')

    # Заголовок "Данные для входа"
    HEADER_LOGIN_DETAILS = (By.CSS_SELECTOR, '#page-right > div > div > div > form > p:nth-child(5)')

    # Поле ввода email или телефона
    ADDRESS_INPUT = (By.ID, 'address')

    # Поле пароля при регистрации
    REGISTRATION_PASSWORD = (By.ID, 'password')

    # Поле подтверждения пароля при регистрации
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, 'password-confirm')

    # Кнопка с текстом "Зарегистрироваться" на странице регистрации
    THE_REGISTER_BUTTON = (By.CSS_SELECTOR, '#page-right > div > div > div > form > button')

    # Ссылка с текстом "Пользовательское соглашение"
    USER_CONCLUSION = (By.CSS_SELECTOR, '#page-right > div > div > div > form > div.auth-policy > a')

    # Текст 'Учетная запись уже используется'
    TEXT_ACCOUNT_RECORDS_USE_USED = (By.CSS_SELECTOR, '#page-right > div > div > div > form > '
                                                      'div.base-modal-wrapper.card-modal > div > div > h2')

    # Кнопка "Войти" в модальном окне под заголовком 'Учетная запись уже используется'
    RETURN_BUTTON = (By.CSS_SELECTOR,
                     '#page-right > div > div > div > form > '
                     'div.base-modal-wrapper.card-modal > div > div > '
                     'div.card-modal__btns > button:nth-child(1)')

    # Текст о том, что код подтверждения телефона был отправлен по указанному номеру
    CONFIRMATION_PHONE_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > h1')

    # Текст ошибки ввода пароля под полем 'Пароль'"
    TEXT_REFERENCE_OF_PASSWORD = (By.CSS_SELECTOR, '#page-right > div > div > div > '
                                                   'form >'
                                                   'div.new-password-container > '
                                                   'div.rt-input-container.rt-input'
                                                   '-container--error.new'
                                                   '-password-container__password > '
                                                   'span')

    # Текст ошибки ввода пароля под полем 'Подтверждения пароля'"
    TEXT_REFERENCE_OF_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR,
                                               '#page-right > div > '
                                               'div > div > form >'
                                               'div.new-password'
                                               '-container >'
                                               'div.rt-input'
                                               '-container.rt-input'
                                               '-container--error.new'
                                               '-password'
                                               '-container__confirmed-password > span')

    # Cсылка с текстом "Политикой конфиденциальности"
    LINK_WITH_TEXT_PRIVACY_POLICY = (By.CSS_SELECTOR, '#rt-footer-agreement-link > '
                                                      'span:nth-child(1)')

    # Cсылка с текстом "Пользовательским соглашением"
    LINK_WITH_TEXT_USER_AGREEMENT = (By.CSS_SELECTOR, '#rt-footer-agreement-link > '
                                                      'span:nth-child(2)')

    # Заголовок статьи политики конфиденциальности
    HEADING_STATE_POLITICS_PRIVACY_POLICY = (By.CLASS_NAME, 'offer-title')

    # Заголовок статьи пользовательского соглашения
    HEADING_ARTICLES_USER_REFERENCES = (By.CLASS_NAME, 'offer-title')

    # Иконка изменения ФИО
    BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                                                  'div.base-card.home__info-card > '
                                                                  'div.user-info.home__user-info > '
                                                                  'div.user-info__edit > button')

    # Текущая фамилия
    CURRENT_LAST_NAME = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                          'div.base-card.home__info-card > '
                                          'div.user-info.home__user-info > '
                                          'div.user-info__name-container > h2 > '
                                          'span.user-name__last-name')

    # Изначальное отчество
    CURRENT_FIRST_NAME_AND_MIDDLE_NAME = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                                           'div.base-card.home__info-card > '
                                                           'div.user-info.home__user-info > '
                                                           'div.user-info__name-container > h2 > '
                                                           'span.user-name__first-patronymic')

    # Поле "Фамилия" внутри ЛК
    USER_LASTNAME = (By.ID, 'user_lastname')

    # Поле "Имя" внутри ЛК
    USER_FIRSTNAME = (By.ID, 'user_firstname')

    # Поле "Отчество" внутри ЛК
    USER_PATRONYMIC = (By.ID, 'user_patronymic')

    # Клик по кнопке сохранения ФИО
    USER_CONTACTS_EDITOR_SAVE = (By.ID, 'user_contacts_editor_save')

    # Тост-уведомление об изменении ФИО
    TOAST_CHANGING_NAME_LAST_NAME_PATRONYMIC = (By.CSS_SELECTOR, 'div > div.rt-toast__content')

    # Явное ожидание текст внутри тост-уведомления
    TEXT_INSIDE_TOAST = (By.CSS_SELECTOR, 'div > div.rt-toast__content > h4')

    # Новое имя и/или отчество
    NEW_FIRST_NAME_AND_PATRONYMIC = (By.CSS_SELECTOR,
                                     '#app > main > div > div.home > div.base-card.home__info-card > '
                                     'div.user-info.home__user-info > div.user-info__name-container > h2 > '
                                     'span.user-name__first-patronymic')

    # Новая фамилия
    NEW_LAST_NAME = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                      'div.base-card.home__info-card > '
                                      'div.user-info.home__user-info > '
                                      'div.user-info__name-container > h2 > '
                                      'span.user-name__last-name')

    # Иконка "Карандаш" для смены пароля
    CHANGING_PASSWORD_ICON = (By.ID, 'password_change')

    # Поле ввода текущего пароля
    CURRENT_PASSWORD = (By.ID, 'current_password')

    # Поле ввода нового пароля
    NEW_PASSWORD = (By.ID, 'new_password')

    # Поле ввода подтверждения пароля
    CONFIRM_PASSWORD = (By.ID, 'confirm_password')

    # Кнопка сохранения пароля
    PASSWORD_SAVE = (By.ID, 'password_save')

    # Ожидание текста ошибки
    USER_PASSWORD_EDITOR_ERROR_TEXT = (By.CSS_SELECTOR, "#app > main > div > div.home > "
                                                        "div.base-card.home__info-card > "
                                                        "div.base-modal.card-modal.user-password-editor > "
                                                        "div > div > div > p.user-password-editor__error")

    # Ожидание текста ошибки входа в ЛК
    FORM_ERROR_MESSAGE = (By.ID, "form-error-message")

    # Текст о том, что фамилия введена невалидная
    LAST_NAME_ERROR_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > '
                                             'div.rt-input-container.rt-input-container--error > span')

    # Текст о том, имя введено невалидное
    FIRST_NAME_ERROR_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > div > form > '
                                              'div.name-container > div:nth-child(1) > span')

    # Заголовок "Учетные данные" внутри личного кабинета
    CREDENTIALS = (By.CSS_SELECTOR, '#app > main > div > div.home > div.base-card.home__info-card > '
                                    'h3:nth-child(2)')

    # Иконка "глаз" для скрытия/открытия пароля
    EYE_ICON_PASSWORD = (By.CSS_SELECTOR,
                         '#page-right > div > div > div > form > div.new-password-container > '
                         'div.rt-input-container.new-password-container__password > div > div.rt-input__action > '
                         'svg')
