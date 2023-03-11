# YATUBE REST API

REST API для проекта Yatube (учебный проект Яндекс.Практикум) 

Создание, редактирование и чтение постов и комментариев в социальной сети Yatube. Добавлена подписка на пользователей. Для аутентификации используется JWT.

- Лёвушкин Никита, когорта 19+
-https://github.com/Rederickmind

### Технологии
Python 3.9.10  
Django 3.2  
Django REST Framework 3.12.4
Simplejwt 4.7.2  
Djoser  

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Rederickmind/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Документация
После запуска проекта документация доступна по адресу 127.0.0.1:8000/redoc

### Примеры работы с API

### Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна в только в режиме чтения
```
GET api/v1/posts/ - получить список всех публикаций.
```
```
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
```
```
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
```
```
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
### Примеры работы с API для авторизованных пользователей
Создание публикации:
```
POST /api/v1/posts/
```

Обновление публикации:
```
PUT /api/v1/posts/{id}/
```

Частичное обновление публикации:
```
PATCH /api/v1/posts/{id}/
```

Удаление публикации:
```
DEL /api/v1/posts/{id}/
```

Доступ авторизованным пользователям доступен по JWT-токену

Получение токена (передаём Username и Password в JSON)
```
POST /api/v1/jwt/create/
```

Обновление JWT-токена:
```
POST /api/v1/jwt/refresh/
```
Проверка JWT-токена:
```
POST /api/v1/jwt/verify/ - проверка JWT-токена
```