REST API-сервис на Django + DRF для управления пользователями и заказами.  

Реализованы:
- регистрация и работа с пользователями;
- CRUD для заказов;
- фильтрация заказов по пользователю (`/orders?user_id=1`);
- поиск, сортировка, пагинация;
- JWT-авторизация;
- автоматическая Swagger-документация.


- Python 
- Django 
- Django REST Framework
- drf-spectacular (Swagger UI)
- SimpleJWT (авторизация)
- django-filter
- Docker + docker-compose



# Запуск
# Docker
```bash
git clone https://github.com/your-repo/cc_ta.git
cd cc_ta
docker-compose up --build
