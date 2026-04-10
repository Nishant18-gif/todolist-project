ToDo List Project

This is a ToDo List web application built with Python, Django, and Django REST Framework.

Features

User authentication (signup, login)

Create, update, delete, and view tasks

Mark tasks as completed or pending

Each user can manage their own tasks

Secure API access with authentication

API Endpoints
Method	URL	Description
POST	/api/register/	Register a new user
POST	/api/login/	Login and obtain authentication token
GET	/api/tasks/	List all tasks for the logged-in user
POST	/api/tasks/	Create a new task
GET	/api/tasks/{id}/	Retrieve a specific task
PUT	/api/tasks/{id}/	Update a specific task
DELETE	/api/tasks/{id}/	Delete a specific task

Note: All endpoints (except /api/register/ and /api/login/) require an Authorization header.

Technologies Used

Python

Django

Django REST Framework

SQLite / PostgreSQL (depending on configuration)

How to Run Locally

Clone the repository:
git clone https://github.com/Nishant18-gif/todolist-project

Navigate to the project directory:
cd todo-project

Create and activate a virtual environment:
python -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Open your browser and go to:
http://127.0.0.1:8000/
