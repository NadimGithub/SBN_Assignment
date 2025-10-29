# SBN_Assignment
# Book Manager — Django + PostgreSQL CRUD Web App

A simple **Book Management Web Application** built with **Python (Django)** and **PostgreSQL**.
This project demonstrates practical skills in full-stack web development, REST API creation, third-party API integration, and basic data visualization.

---

##  Features

 **CRUD Operations:**
Add, view, update, and delete books.

 **REST APIs:**
All CRUD functions are accessible via REST API endpoints.

**Third-Party API Integration:**
Fetch book details (title and author) automatically from **OpenLibrary API** using an ISBN number.

 **Dashboard with Data Visualization:**
Interactive chart showing the number of books per author using **Chart.js**.

 **Responsive Frontend:**
Fully responsive Bootstrap 5-based interface with modern design.

---

##  Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, Bootstrap 5, Chart.js
* **Database:** PostgreSQL (local)
* **API Integration:** OpenLibrary API
* **Deployment:** Local environment

---

##  Installation Guide

###  Clone the repository

```bash
git clone https://github.com/<your-username>/book-manager.git
cd book-manager
```

###  Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
```

###  Install dependencies

```bash
pip install -r requirements.txt
```

###  Configure PostgreSQL database

Create a PostgreSQL database (e.g. `book_db`) and update your **settings.py**:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'book_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

###  Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

###  Create a superuser (optional)

```bash
python manage.py createsuperuser
```

###  Run the server

```bash
python manage.py runserver
```

Open your browser at
 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

##  Application Structure

```
book_manager/
│
├── books/                    # Main app
│   ├── migrations/
│   ├── templates/books/
│   │   ├── base.html
│   │   ├── book_list.html
│   │   ├── book_form.html
│   │   ├── book_detail.html
│   │   └── dashboard.html
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   └── api_views.py
│
├── book_manager/             # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

---

##  API Endpoints

| Method | Endpoint                                | Description                             |
| ------ | --------------------------------------- | --------------------------------------- |
| GET    | `/api/books/`                           | List all books                          |
| POST   | `/api/books/`                           | Create a new book                       |
| GET    | `/api/books/<id>/`                      | Retrieve a single book                  |
| PUT    | `/api/books/<id>/`                      | Update a book                           |
| DELETE | `/api/books/<id>/`                      | Delete a book                           |
| GET    | `/books/fetch_openlibrary/?isbn=<isbn>` | Fetch book details from OpenLibrary API |

---

##  Dashboard Overview

* Total Books
* Number of Authors
* Recently Added Books
* Interactive Bar Chart — Books count per Author

---

##  How It Works

1. Enter ISBN → Click “Fetch by ISBN” → App retrieves details from **OpenLibrary API**.
2. Fill in or edit remaining fields → Save book entry.
3. Dashboard displays summary cards and author chart.
4. All books can be viewed, updated, or deleted through a responsive web UI or API.

---

##  Example OpenLibrary API Response

When user clicks **“Fetch by ISBN”**, request is sent to:

```
https://openlibrary.org/isbn/<isbn>.json
```

Response contains title and author fields used to auto-fill the form.

