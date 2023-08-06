# Auto Marketplace

Auto Marketplace - it's marketplace for customers and sellers of auto-goods.

## Install

---
1. Clone the repository:

```
$ git clone https://github.com/may42day/auto-marketplace
$ cd auto-marketplace
```
2. Fill in .env file or use .env_example:
```
$ mv .env_example .env
```

3. Build docker containers:
```
$ docker-compose up -d
```
3. Run migrations:
```
$ docker exec -it auto-marketplace_backend_1 bash
$ python manage.py makemigrations
$ python manage.py migrate

```
4. Application started. Navigate to http://127.0.0.1:8000
_Note that market page is empty untill you upload a content._

Follow instructions below to run only the application:

1. Repeat steps 1,2 above
2. Create a virtual environment:

```
$ python -m venv venv
$ source venv/bin/activate
```

3. Install the dependencies:

```
(venv)$ pip install -r requirements.txt
```

4. Run server and navigate to http://127.0.0.1:8000

```
(venv)$ python manage.py runserver
```

## Apps

---

The project consists of the following apps:

:busts_in_silhouette: users \
Registration, sellerss goods.

:wrench:goods\
Products by categories, search, product cards, products moderation.

:rage:feedback\
Feedback system.

:package:cart\
Shopping cart and orders history.

## Requirements

---

:clipboard:[Requirements](https://github.com/may42day/)

## Author

---

:mailbox:[Vlad Hodorovich](https://www.linkedin.com/in/may42day/).

## License

---

:bookmark_tabs: The project is available under the terms of the [MIT License](https://github.com/may42day/auto-marketplace/blob/main/LICENSE).
