 Todo List Management System

This is a Todo List Management web application built with Python and Django. It allows users to create, manage, and track their daily tasks with authentication and user-specific access.

 Features
User authentication (signup, login)
Create tasks / todos
View all tasks
Update and edit tasks
Delete tasks
Mark tasks as completed / pending
User-specific task management (each user sees only their tasks)
🔗 API Endpoints 
Method	URL	Description
POST	/register/	Register a new user
POST	/login/	Login user
GET	/tasks/	List all tasks
POST	/tasks/	Create a new task
PUT	/tasks/{id}/	Update a task
DELETE	/tasks/{id}/	Delete a task
🛠️ Technologies Used
Python
Django
SQLite (database)
Django Authentication System
🚀 How to Run Locally
1. Clone the repository:
git clone https://github.com/Nishant18-gif/todolist-project.git
2. Navigate to the project directory:
cd todo-project
3. Create and activate virtual environment:

Windows:

python -m venv venv
venv\Scripts\activate

macOS/Linux:

source venv/bin/activate
4. Install dependencies:
pip install -r requirements.txt
5. Apply migrations:
python manage.py migrate
6. Run the server:
python manage.py runserver
7. Open in browser:
http://127.0.0.1:8000/
⚠️ Notes
Make sure Python is installed on your system
Activate virtual environment before running project
Ensure db.sqlite3 is ignored using .gitignore
Update .env file if required
👨‍💻 Author

Nishant Pareek

GitHub: https://github.com/Nishant18-gif
