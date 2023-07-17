#  Итоговый проект по автоматизации тестирования
## Объект тестирования: [Ростелеком](https://b2c.passport.rt.ru)

### Для тестирования сайта были использованы
- мануальные и автоматизированные тесты

### Используемые библиотеки и модули
Faker 19.1.0 \
Pytest 7.3.2 \
Selenium 4.10.0 

random \
platform \
getpass


### Почему именно эти инструменты использовались
При выборе инструментов для тестирования сайта учитывалась функциональность, удобство использования и соответствие требованиям проекта. 
**Pytest** и **Selenium** позволяют автоматизировать тесты веб-сайта, **Faker** обеспечивает создание реалистичных тестовых данных, 
**random** помогает генерировать разнообразные случайные значения. **Platform** необходим для определения OS на запускаемой машине для правильного подбора горячих клавиш Selenium.
**Getpass** используется чтобы обратиться к запускающему лицу по имени пользователя его машины, если тесты упадут.

### Используемые техники тест-дизайна
- Классы эквивалентности 
- Граничные значения
- Тестирование состояний и переходов

### Почему именно эти техники тест-дизайна использовались
* Техника классов эквивалентности позволяет разделить входные данные на группы, которые имеют одинаковое поведение. Это помогает сократить количество тестовых случаев, которые требуется проверить. 
* Тестирование граничных значений направлено на проверку поведения при крайних значениях входных данных или параметров. Например, минимальные и максимальные значения пароля при регистрации. Граничные значения часто вызывают особые ситуации или ошибки, и их тестирование позволяет выявить потенциальные проблемы на сайте.
* Техника тестирования состояний и переходов позволяет проверить какой-либо функционал сайта в разных состояниях системы или ее компонентов. Например, различные состояния формы ввода данных или навигации по страницам. Проверка переходов между состояниями помогает выявить ошибки, убедиться в правильном функционировании и корректности работы сайта при различных ситуациях.

В теории эти техники помогают обеспечить хорошее покрытие тестирования и эффективно выявлять дефекты на сайте.

### Тест-кейсы и баг-репорты
[Доступны по этой ссылке](https://docs.google.com/spreadsheets/d/1R30jt8g9oHbXQ8hR1CeaHae3VhmGYdo9Al4J4S5tJjg/edit?usp=sharing) \
_Переключение между листами внизу документа_ \
Общее количество тест-кейсов: 22 \
Общее количество автотестов: 22 \
Общее количество баг-репортов: 4

### IDE
PyCharm Community 2023.1.4
Aqua 2023.1 Public Preview

### Окружение 
Версия 114.0.5735.199 (Официальная сборка), (64 бит)   
Windows 11, Версия 22H2

### Архитектура проекта
Приоритетом являлись следующие принципы разработки ПО: DRY, KISS, YAGNI, некоторые принципы SOLID.


#### Папка Classes
* Characters_generator.py - Содержит генераторы некоторых паролей и отдельных символов, для которых не подходит библиотека Faker
* Data_for_Assert.py - Собраны тексты для ассертов в тестах
* FakePerson.py - Генерация необходимых тестовых данных: имени, фамилии, отчества и телефона
* Stability - Содержит классы, прямо либо косвенно связанных со стабильностью тестов

#### Папка tests
* test_changing_data_inside_your_account.py - Содержит позитивные и негативные тесты, изменяющие данные пользователя внутри личного кабинета
* test_create_account.py - Содержит негативные и позитивные тесты, связанные с регистрацией пользователя
* test_login_to_personal_account.py - Включает позитивные и негативные тесты, которые проверяют вход в личный кабинет
* test_others.py - Всё, что не вошло которые не вошли в другие модули

#### Другие файлы в корневой папке
* conftest.py - содержит фикстуру инициализации и закрытия браузера
* requirements.py - используемые импортируемые библиотеки проекта
* credentials.py - адрес самого сайта, валидные и некоторые невалидные данные для входа в личный кабинет
* .gitignore - игнорируемые файлы и папки Git
* README.md - файл, описывающий проект, которые вы сейчас прочитали
