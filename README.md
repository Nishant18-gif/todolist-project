Todo List Management System

A task management web application built with Python and Django. It allows users to create, manage, and update daily tasks with authentication and user-specific access. Tasks can have a priority (high, medium, low) and can be filtered by completion status and priority.

Features
User authentication (signup, login)
Create, view, update, delete tasks
Mark tasks as completed
Set priority for tasks (high, medium, low)
Filter tasks by status (completed / incomplete) and priority
User-specific task management (users can only manage their own tasks)
JSON API responses for frontend integration
Proper error handling (404, 401, 405, etc.)
API Endpoints with Examples
1. Register User
Method: POST
URL: /auth/register/

Body (x-www-form-urlencoded):

username: john
password: 1234

Response:

{
    "message": "Signup successful"
}
2. Login User
Method: POST
URL: /auth/login/

Body:

username: john
password: 1234

Response:

{
    "message": "Login successful",
    "token": "9e946cd5-1975-4baa-adf4-b63b77235bc3"
}
3. List Tasks
Method: GET
URL: /api/tasks/

Header:

Authorization: Bearer <token>
Optional Query Params:
status=completed / status=incomplete
priority=high / priority=medium / priority=low

Response:

{
    "status": true,
    "code": 200,
    "message": "Tasks fetched",
    "tasks": [
        {
            "id": 1,
            "title": "Buy milk",
            "completed": false,
            "priority": "medium",
            "user_id": 1
        }
    ]
}
4. Add Task
Method: POST
URL: /api/tasks/add/

Header:

Authorization: Bearer <token>

Body (x-www-form-urlencoded):

title: Learn Django
completed: false
priority: high

Response:

{
    "status": true,
    "code": 200,
    "message": "Task added"
}
5. Update Task
Method: POST
URL: /api/tasks/update/<task_id>/

Header:

Authorization: Bearer <token>

Body (x-www-form-urlencoded, optional fields):

title: Learn Django REST
completed: true
priority: medium

Response:

{
    "status": true,
    "code": 200,
    "message": "Task updated"
}
6. Delete Task
Method: POST
URL: /api/tasks/delete/<task_id>/

Header:

Authorization: Bearer <token>

Response:

{
    "status": true,
    "code": 200,
    "message": "Task deleted"
}
Technologies Used
Python 3.x
Django 4.x
SQLite (database)
Django Authentication System
HTML, CSS (optional frontend)
How to Run Locally

Clone the repository:

git clone https://github.com/Nishant18-gif/todolist-project.git

Navigate to the project directory:

cd todolist-project

Create and activate a virtual environment:

python -m venv venv
On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Open your browser:

http://127.0.0.1:8000/
Notes
Make sure Python 3.x is installed
Always activate the virtual environment before running the project
All API responses are JSON for easy frontend integration
Update .env file if required
Author

Nishant Pareek
GitHub: https://github.com/Nishant18-gif
