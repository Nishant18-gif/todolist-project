Todo List Management System

This is a task management web application built with Python and Django. It allows users to create, manage, and update daily tasks with authentication and user-specific access.

Features
User authentication (signup, login)
Create new tasks
View all tasks
Update and edit tasks
Delete tasks
Mark tasks as completed
User-specific task management (users can manage their own tasks)
API Endpoints (if applicable)

Method | URL | Description
POST | /register/ | Register a new user
POST | /login/ | Login user
GET | /tasks/ | List all tasks
POST | /tasks/ | Create a new task
PUT | /tasks/{id}/ | Update a task
DELETE | /tasks/{id}/ | Delete a task

Technologies Used
Python
Django
SQLite (database)
Django Authentication System
HTML
CSS
How to Run Locally

Clone the repository:

git clone https://github.com/Nishant18-gif/todolist-project.git

Navigate to the project directory:

cd todolist-project

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

Notes
Make sure Python is installed on your system
Ensure virtual environment is activated before installing dependencies
Update .env file if required
Author

Nishant Pareek

GitHub: https://github.com/Nishant18-gif
