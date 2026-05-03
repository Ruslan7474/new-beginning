## Наш второй сайт - интернет магазин с группой 1-24

### Инструкции по установке тем у кого Windows
### скачиваем этот проект через команду 
#### git clone https://github.com/edzen12/AutoShop.git
### открываем в VSCode, открываем терминал и пишем команду 
#### python -m venv venv
#### .\venv\Scripts\activate
#### pip install -r requirements.txt
#### python manage.py migrate
#### python manage.py createsuperuser
#### python manage.py runserver

### Инструкции по установке тем у кого MacOS/Linux
### скачиваем этот проект через команду 
#### git clone git@github.com:edzen12/AutoShop.git
### открываем в VSCode, открываем терминал и пишем команду 
#### python3 -m venv venv
#### source venv/bin/activate
#### pip install -r requirements.txt
#### python manage.py migrate
#### python manage.py createsuperuser
#### python manage.py runserver