#  Todo List Management System

This is a Todo List Management web application built with Python and Django. It allows users to create, manage, and track their daily tasks with authentication and user-specific access.

---

##  Features

- User authentication (signup, login)
- Create tasks / todos
- View all tasks
- Update and edit tasks
- Delete tasks
- Mark tasks as completed / pending
- User-specific task management (each user sees only their tasks)

---

## 🔗 API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/register/` | Register a new user |
| POST | `/login/` | Login user |
| GET | `/tasks/` | List all tasks |
| POST | `/tasks/` | Create a new task |
| PUT | `/tasks/{id}/` | Update a task |
| DELETE | `/tasks/{id}/` | Delete a task |

---

##  Technologies Used

- Python
- Django
- SQLite (database)
- Django Authentication System

---

##  How to Run Locally

Clone the repository:
```bash
git clone https://github.com/Nishant18-gif/todolist-project.git

Navigate to project:

cd todo-project

Create virtual environment:

python -m venv venv
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Start server:

python manage.py runserver

Open browser:

http://127.0.0.1:8000/
 Notes
Make sure Python is installed
Activate virtual environment before running
Ensure .gitignore is properly set
 Author

Nishant Pareek
GitHub: https://github.com/Nishant18-gif
