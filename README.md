# :clown_face: API для Yatube :clown_face: #
## Описание:
Работайте с помощью API с вашими постами, комментариями и подписками на Yatube. Также можно просматривать группы.  
  
Все 6 CRUD операций доступны для:
* постов
* комментариев  


Для подписок доступны операции:
- List
- Create  


Для групп доступны операции:
- List
- Retrieve


## Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Delicate1pants/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение (пример для Windows):

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


## Где найти примеры запросов:
После запуска сервера, будет доступна актуальная документация по адресу http://127.0.0.1:8000/redoc/ (пример для локального запуска сервера)  
  
Там будут подробно описаны примеры запросов
