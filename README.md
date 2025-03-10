### 👋Для связи - пишите разработчику в TG: [@zakRash123](https://t.me/zakRash123) 

# 🚀 Crypto WebSOCKET Django PROJECT

## 📖 Описание проекта

Этот проект представляет собой Django-приложение, которое получает данные о криптовалюте из **Binance WebSOCKET API**  
Версия PYTHON 3.10
Проект разрабатывался в среде Линукс (Убунту 22.04), рекомендовано  запускать на идентичной ОС

✅ Транслирует их на фронтенд через WebSOCKET.  
✅ Записывает данные в базу каждые **15 секунд**.  

Применяются **Django Channels**, **PGSQL** и **Redis** для обработки WebSOCKET-подключений.

---

## 🎯 Функционал проекта

🔹 Подключение к WebSOCKET Binance API: `wss://stream.binance.com:9443/ws/btcusdt@trade`.  
🔹 Передача цен на BTC/USDT в **реальном времени** через WebSOCKET.  
🔹 Сохранение цен в базу данных каждые **15 секунд**.  
🔹 Django API для получения исторических данных.  
🔹 Тесты с использованием `pytest`, `pytest-django`, `pytest-asyncio`.  

---

## 📌 Установка и настройка

### Клонирование проекта
```
git clone https://github.com/TrueAirRash/binance_ws_api_asker.git
cd binance_ws_api_asker
```
## Настройка виртуального окружения
```
python3 -m venv venv
source venv/bin/activate  # для Linux
```
## Установка зависимостей
```
pip install -r requirements.txt
```
## Настройка базы данных
Используется POSTGRESQL, поэтому сначала следует установить и запусти сервер. Затем сделать базу данных. Из первичных действий этого подраздела - это:
```
sudo apt update
sudo apt install postgresql postgresql-contrib
```
затем выполнить:
```
sudo -u postgres psql
```
После этого шага в открывшейся интерактивной консоли PGSQL выполнить слкдующие команды:
```
CREATE DATABASE crypto_db;
CREATE USER crypto_user WITH PASSWORD 'my_pass_123';
ALTER ROLE crypto_user SET client_encoding TO 'utf8';
ALTER ROLE crypto_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE crypto_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE crypto_db TO crypto_user;
```

## Применение миграций
```
python manage.py migrate
```
## Запуск сервера Django и Запуск WebSOCKET-сервера
Из корня проекта выполнить:
```
python3 manage.py runserver
```
и (для работы WebSOCKET в Django Channels используй Daphne):
```
daphne -b 0.0.0.0 -p 8001 cryp_proj.asgi:application
```
Затем с рабочей машины перейти на 
```
http://127.0.0.1:8000/
```
Или на 
```
http://127.0.0.1:8000/prices
```


## Тестирование проекта
Проект использует 
```
pytest, pytest-asyncio, pytest-django.
```

✅ Для корректного прохождения тестирования необходимо:
перейти в PGSQL, выполнив:  
```
sudo -u postgres psql
```
в открывшейся консоли PGSQL выполнить: 
```
\du
```
пользователю, фигурирующему в  settings.py (crypto_user), дать соответствующие права: 
```
ALTER USER crypto_user CREATEDB;
```

✅ Запуск всех тестов. Из корня проекта выполнить:
```
pytest
```

### 👋Для связи - пишите разработчику в TG: [@zakRash123](https://t.me/zakRash123) 


