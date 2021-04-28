# fabrique_test_polls
Скачать или клонировать проект.

Дальше работа в терминале, приведены команды.

Создать в корневом каталоге(на одном уровне вложенности с папкой fabrique_polls_test) виртуальную среду:

"python3 -m venv env"

Запустить виртуальную среду командой:

"source env/bin/activate" - для линукс.

Перейти по пути:

"cd fabrique_polls_test/"

Установить зависимости:

"pip install -r requirements.txt"

Создать и применить миграции:

"python manage.py makemigrations" ,
"python manage.py migrate"

Создать суперпользователя:

"python manage.py createsuperuser"

Запустить сервер:

"python manage.py runserver"

Запустится локальный сервер доступный по адрессу:

"http://127.0.0.1:8000/"

Авторизация происходит по пути:

"auth/login/"

API доступно по пути:

"api/v1/polls/"

Функционал доступный администратору:

"admin_create_polls/" - Создание опроса.

"admin_create_questions/" - создание вопроса.

"admin_update_polls/<int:pk>" - редактирование опроса.

"admin_update_questions/<int:pk>" - редактирование вопроса.

Функционал доступный пользователю:

"user_get_polls/" - получение списка опросов.

"try_poll/" - прохождение опросов.

"user_poll/<int:id>/" - получение пройденных опросов по ID пользователя.




 
 
