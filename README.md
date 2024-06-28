* активируйте виртуальное окружение:
```
python3 -m venv venv
sourse venv/bin/activate
```
* установите зависимости
```
pip install -m requrements.txt
```
* создайте файл `.env`. Скопируйте из `.env_example` поля в `.env` и подставьте необходимые значения. 

* синзнизируйте ваш код с базой данных:
```
- python manage.py makemigrations
- python manage.py migrate
```
* Запустите парсер фотографий и алгоритм извлечения признаков

```
- python perser.py
- python searc_algo.py
```


* Запустите проект
```
- python manage.py runserver
```

* Обратитесь по адресу `http://127.0.0.1:8000/api/products/` и отправите фотографию для поиска через form-data
