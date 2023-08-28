# QRKot_spreadsheet

### Описание
Проект QRKot — это благотворительный фонд поддержки котиков. Его назначение — собирать пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
### Возможности Google_APIs
В данной версии добавлена возможность формирования google таблицы с актуальными
данными о закрытых проектах фонда.
Формирование данных в google таблицы происходит с помощью POST запроса по адресу
http://localhost/google

### Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=008000)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=008000)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/-Pydantic-464646?style=flat&logo=Pydantic&logoColor=ffffff&color=008000)](https://docs.pydantic.dev/latest/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=FastAPI&logoColor=ffffff&color=008000)](https://fastapi.tiangolo.com/)
[![GoogleCloudAPIs](https://img.shields.io/badge/-GoogleCloudAPIs-464646?style=flat&logo=GoogleCloudAPIs&logoColor=ffffff&color=008000)](https://cloud.google.com/apis/docs/overview)
## Запуск проекта
```
git clone 
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

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
Создайте файл .env в корневой директории со следующим содержимым:
```
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db                             
SECRET=SECRET_KEY
FIRST_SUPERUSER_EMAIL=user@gmail.com
FIRST_SUPERUSER_PASSWORD=admin
```
А также добавьте в файл .env данные своего
сервисного аккаунта полученные из json файла
на платформе GoogleCloudAPIs
```
TYPE=
PROJECT_ID=
PRIVATE_KEY_ID=
PRIVATE_KEY=
CLIENT_EMAIL=
CLIENT_ID=
AUTH_URI=
TOKEN_URI=
AUTH_PROVIDER_X509_CERT_URL=
CLIENT_X509_CERT_URL=
UNIVERSE_DOMAIN=
```

Запустите проект
```
uvicorn app.main: app --reload
```
После запуска, проект будет доступен по адресу http://localhost/

Документация Swagger доступна по адресу http://localhost/docs
Документация Redoc доступна по адресу http://localhost/redoc

### Автор
Сободаж Антон