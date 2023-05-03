# Тестирование авторизации ЛК Ростелеком
___
Объект тестирования: [Авторизация в ЛК Ростелеком](https://b2c.passport.rt.ru/)
#### [**ТЕСТ КЕЙСЫ и БАГРЕПОРТЫ**](https://docs.google.com/spreadsheets/d/1Tr2CPqKxw1jVNKdVe3R4P9kUYSdRV4WQdQFcOYRA2kA/edit?usp=sharing)

:red_circle: При тестировании применялись следующие техники тест-дизайна:
- Таблица принятия решений
- Эквивалентное разделение
- Граничные значения
___
### Тестирование требований
#####  ✨ В требованиях не указано
- На странице авторизации:
    - Шапка страницы с логотипом РТ
    - Кнопка показать пароль
    - Чекбокс "Запомнить меня"
    - Ссылка "Забыл пароль"
    - Ссылка на пользовательское соглашение
    - Ссылка зарегистрироваться
    - Раздел авторизации через соцсети OAuth (логотипы)
        - VK
        - OK
        - Mail
        - Google
        - Ya
    - Наличие подвала страницы
        - Copyright
        - Согласие на обработку Cookie и ссылка на пользовательское соглашение
        - Телефон службы поддержки
- При каких условиях появляется подтверждение через капчу.

___

## Структура проекта

:file_folder: **pages** - PageObject + pages instance
 - :clipboard: base.py - PageObject WebPage base class (статика)
 - :clipboard: elements.py - PageObject WebElement class (статика)
 - :clipboard: RTForgotPass.py - страница "Забыл пароль", класс доступа к странице и элементам на ней с локаторами
 - :clipboard: __RTMain.py__ - главная страница авторизации, класс доступа к странице и элементам на ней с локаторами
 - :clipboard: RTOauthResult.py - страница результата OAuth авторизации, класс доступа к странице и элементам на ней с локаторами
 - :clipboard: RTRegister.py - страница "Зарегистрироваться", класс доступа к странице и элементам на ней с локаторами

:file_folder: **tests** - Тесты 
 - :clipboard: test_negative_auth.py - негативные
 - :clipboard: test_positive_auth.py - позитивные
 - :clipboard: helpers.py - вспомогательные функции

:file_folder: **screenshots** - скриншоты упавших тестов 

:clipboard: credentials.py - статичные данные для авторизации + Faker для регистрации

___

## Запуск тестов

### Подготовка
- Установить зависимости
```sh
cd Mod28_HW_Fin
pip install -r requirements.txt
```
- Установить Chrome driver

```sh
pip install -r requirements.txt
```

### Непосредственно запуск
- Все тесты:
```sh
py.test.exe --driver Chrome
```
- Все тесты из определенного файла:
```sh
py.test.exe --driver Chrome tests/test_positive_auth.py
py.test.exe --driver Chrome tests/test_negative_auth.py
```
- Конкретный тест:
```sh
py.test.exe --driver Chrome tests/test_positive_auth.py::test_authpage_form
```
- Тесты в наименовании которых есть (нет) подстрока:
```sh
py.test.exe --driver Chrome -k "authpage_form"
```

- Только строго маркированные:
```sh
py.test.exe --driver Chrome -m "smoke and not reg"
py.test.exe --driver Chrome -m "smoke and auth"
py.test.exe --driver Chrome -m "positive"
py.test.exe --driver Chrome -m "negative"
py.test.exe --driver Chrome -m "negative and regress"
```

#### Возможные маркеры:

| Mark     |        Type        |
|----------|:------------------:|
| smoke    |    Smoke tests     |
| auth     |     Auth tests     |
| front    |    Frontend UI     |
| reg      | Registration tests |
| positive |  Positive tests    |
| negative |   Negative tests   |
| regress  |  Regression tests  |


## License

MIT

