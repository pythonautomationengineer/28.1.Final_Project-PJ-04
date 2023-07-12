from selenium.webdriver.common.by import By


class Selectors:
    """Селекторы для тестов"""

    CAPTCHA_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > div > form > div.rt-captcha.login-form__captcha > '
                                     'div.rt-input-container.rt-captcha__input > span')

    TAB_PHONE_BUTTON = (By.ID, 't-btn-tab-phone')
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'kc-login')

    TAB_EMAIL_BUTTON = (By.ID, 't-btn-tab-mail')
    TAB_LOGIN_LOGIN = (By.ID, 't-btn-tab-login')

    LINK_WITH_THE_TEXT_REGISTER = (By.ID, 'kc-register')

    H1_REGISTRATION = (By.CSS_SELECTOR, '#page-right > div > div > h1')

    HEADING_PERSONAL_DATA = (By.CSS_SELECTOR, '#page-right > div > div > div > form > p:nth-child(1)')

    FIRST_NAME_INPUT = (By.CSS_SELECTOR,
                        '#page-right > div > div > div > form > div.name-container > div:nth-child('
                        '1) >'
                        'div > input')

    LAST_NAME_INPUT = (By.CSS_SELECTOR,
                       '#page-right > div > div > div > form > div.name-container > div:nth-child('
                       '2) > div > input')

    REGION_INPUT = (By.CSS_SELECTOR,
                    '#page-right > div > div > div > form > '
                    'div.rt-select.rt-select--search.register-form__dropdown > div > div > input')

    HEADER_LOGIN_DETAILS = (By.CSS_SELECTOR, '#page-right > div > div > div > form > p:nth-child(5)')

    ADDRESS_INPUT = (By.ID, 'address')

    REGISTRATION_PASSWORD = (By.ID, 'password')
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, 'password-confirm')

    USER_CONCLUSION = (By.CSS_SELECTOR, '#page-right > div > div > div > form > div.auth-policy > a')

    THE_REGISTER_BUTTON = (By.CSS_SELECTOR, '#page-right > div > div > div > form > button')

    TEXT_ACCOUNT_RECORDS_USE_USED = (By.CSS_SELECTOR, '#page-right > div > div > div > form > '
                                                      'div.base-modal-wrapper.card-modal > div > div > h2')

    RETURN_BUTTON = (By.CSS_SELECTOR,
                     '#page-right > div > div > div > form > '
                     'div.base-modal-wrapper.card-modal > div > div > '
                     'div.card-modal__btns > button:nth-child(1)')

    CONFIRMATION_PHONE_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > h1')

    TEXT_REFERENCE_OF_PASSWORD = (By.CSS_SELECTOR, '#page-right > div > div > div > '
                                                   'form >'
                                                   'div.new-password-container > '
                                                   'div.rt-input-container.rt-input'
                                                   '-container--error.new'
                                                   '-password-container__password > '
                                                   'span')

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

    LINK_WITH_TEXT_PRIVACY_POLICY = (By.CSS_SELECTOR, '#rt-footer-agreement-link > '
                                                      'span:nth-child(1)')

    LINK_WITH_TEXT_USER_AGREEMENT = (By.CSS_SELECTOR, '#rt-footer-agreement-link > '
                                                      'span:nth-child(2)')

    HEADING_STATE_POLITICS_PRIVACY_POLICY = (By.CLASS_NAME, 'offer-title')
    HEADING_ARTICLES_USER_REFERENCES = (By.CLASS_NAME, 'offer-title')

    BUTTON_CHANGING_NAME_LAST_NAME_PATRONYMIC = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                                                  'div.base-card.home__info-card > '
                                                                  'div.user-info.home__user-info > '
                                                                  'div.user-info__edit > button')

    CURRENT_LAST_NAME = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                          'div.base-card.home__info-card > '
                                          'div.user-info.home__user-info > '
                                          'div.user-info__name-container > h2 > '
                                          'span.user-name__last-name')

    CURRENT_FIRST_NAME_AND_MIDDLE_NAME = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                                           'div.base-card.home__info-card > '
                                                           'div.user-info.home__user-info > '
                                                           'div.user-info__name-container > h2 > '
                                                           'span.user-name__first-patronymic')

    USER_LASTNAME = (By.ID, 'user_lastname')
    USER_FIRSTNAME = (By.ID, 'user_firstname')
    USER_PATRONYMIC = (By.ID, 'user_patronymic')

    USER_CONTACTS_EDITOR_SAVE = (By.ID, 'user_contacts_editor_save')
    TOAST_CHANGING_NAME_LAST_NAME_PATRONYMIC = (By.CSS_SELECTOR, 'div > div.rt-toast__content')
    TEXT_INSIDE_TOAST = (By.CSS_SELECTOR, 'div > div.rt-toast__content > h4')

    NEW_FIRST_NAME_AND_PATRONYMIC = (By.CSS_SELECTOR,
                                     '#app > main > div > div.home > div.base-card.home__info-card > '
                                     'div.user-info.home__user-info > div.user-info__name-container > h2 > '
                                     'span.user-name__first-patronymic')

    NEW_LAST_NAME = (By.CSS_SELECTOR, '#app > main > div > div.home > '
                                      'div.base-card.home__info-card > '
                                      'div.user-info.home__user-info > '
                                      'div.user-info__name-container > h2 > '
                                      'span.user-name__last-name')

    CHANGING_PASSWORD_ICON = (By.ID, 'password_change')
    CURRENT_PASSWORD = (By.ID, 'current_password')
    NEW_PASSWORD = (By.ID, 'new_password')
    CONFIRM_PASSWORD = (By.ID, 'confirm_password')
    PASSWORD_SAVE = (By.ID, 'password_save')

    USER_PASSWORD_EDITOR_ERROR_TEXT = (By.CSS_SELECTOR, "#app > main > div > div.home > "
                                                        "div.base-card.home__info-card > "
                                                        "div.base-modal.card-modal.user-password-editor > "
                                                        "div > div > div > p.user-password-editor__error")

    FORM_ERROR_MESSAGE = (By.ID, "form-error-message")

    LAST_NAME_ERROR_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > div > form > div.name-container > '
                                             'div.rt-input-container.rt-input-container--error > span')

    FIRST_NAME_ERROR_TEXT = (By.CSS_SELECTOR, '#page-right > div > div > div > form > '
                                              'div.name-container > div:nth-child(1) > span')

    CREDENTIALS = (By.CSS_SELECTOR, '#app > main > div > div.home > div.base-card.home__info-card > '
                                    'h3:nth-child(2)')

    EYE_ICON_PASSWORD = (By.CSS_SELECTOR,
                '#page-right > div > div > div > form > div.new-password-container > '
                'div.rt-input-container.new-password-container__password > div > div.rt-input__action > '
                'svg')
