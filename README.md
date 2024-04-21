# Тестовое задание для Anverali

## Требования
- Django==5.0.4
- PostgresSQL
- python>=3.8
## Установка
1. Настроить БД PostgreSQL
    При необходимости создать таблицу командой:
    ```shell
    CREATE DATABASE myproject;
   ```
   Дать права пользователю на таблицу командой:
    ```shell
    GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
    ```
2. Войти в виртуальное окружение, например `source env/bin/activate`
3. Установить зависимости командой `pip install -r requirements.txt`
## Настройка
1. Создать файл с переменными окружения директории `kwork` в виде:
    ```
    SECRET_KEY=[secert key]
    DEBUG=True
    ALLOWED_HOSTS='localhost,127.0.0.1'
    DB_ENGINE='django.db.backends.postgresql'
    DB_NAME=[db name]
    DB_USER=[usename]
    DB_PASSWORD=[user password]
    DB_HOST='localhost'
    DB_PORT=5432
    ```
2. Применить миграции командой:
    ```shell
    python manage.py migrate
    ```
3. Создать суперпользователя командой:
    ```shell
    python manage.py createsuperuser
    ```
## Использование

Для запуска используем команду: `python manage.py runserver`

По адресу `http://127.0.0.1:8000` будет рабочий сайт

## Реализованный функционал
- Простой фронтэнд (лендинг)
- Кабинет заказчика и фрилансера 
- Админ панель Django