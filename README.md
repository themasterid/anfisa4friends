## Проект, Анфиса для друзей в рамках вступительной части Яндекс Практикум бекенд разработчика Python

Проект ознакомительный финального задания вступительной части Яндекс Практикум бекенд разработчика Python.

Все как обычно, клонируем, ставим виртуальное окружение, активируем виртуальное окружение, устанавливаем зависимости, это Django и requests, запускаем сервер:

1.
```bash
git clone https://github.com/themasterid/anfisa4friends.git
```
2.
```bash
python3 -m venv venv
```
3.
```bash
source venv/bin/activate
```
4.
```bash
pip install -r requirements.txt
```
5.
```bash
python manage.py makemigrations
python manage.py migrate
```
6.
```bash
python manage.py runserver
```
Сервер запущен по адресу 127.0.0.1:8000

Пользуемся.
