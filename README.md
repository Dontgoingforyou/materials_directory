# Materials Directory

## Описание
Это приложение для управления категориями и материалами. Оно позволяет загружать данные о категориях и материалах из Excel файла, сохранять их в базе данных и просматривать дерево категорий с подсчетом общей стоимости материалов. 

## Стек технологий
- Python 3.x
- Django
- Django REST Framework
- OpenPyXL
- PostgreSQL
- Postman

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Dontgoingforyou/materials_directory.git
   cd materials_directory

2. Установите зависимости:
   ```bash
   poetry install

3. Настройте БД с помощью .env.sample

4. Примените миграции для инициализации БД:
   ```bash
   python manage.py migrate

5. Запустите сервер разработки:
   ```bash
   python manage.py runserver

6. В директории проекта лежит файл materials.xlsx, можете использовать его для загрузки данных