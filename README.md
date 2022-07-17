# ks_db
Проект работает на Djnago

Для запуска проекта в локальном режиме:

MAC/Linux:
python3 -m venv venv
source venv/bin/activate
pip -r requirements.txt

Windows:
python -m venv venv
source venv/Scripts/activate

Установить PostgreSQL
Получить ключи для Google Drive API


Для запуска локального сервера:
cd ks_db
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver

Что я смог реализовать:
Для меня конечно это задание было сложнее, чем я думал. Но я старался, хотя конечно этого точно не достаточно для полноценной работы. 
На главной странице отображается таблица, которая формируется из базы данных. Есть ссылка, при нажатии на которую БД обнавляется. Реализовать обновление данных онлайн у меня не удалось. 

В корневом каталоге есть файл postgres.py, в котором содержатся функции для создания/удаления/дообавления данных без Django ORM.
В директории приложения supplies: 
Cкрипт sheets.py, который считывает данные из таблицы Google Sheets. 
Скрипт cbr.py, который получает курс доллара с сайта ЦБ РФ.