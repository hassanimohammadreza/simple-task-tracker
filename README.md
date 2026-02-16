# 🗂 Task Tracker – Flask Based Todo Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![License](https://img.shields.io/badge/License-MIT-green)

A clean and modular **Task Tracking Web Application** built with Flask.  
This project demonstrates Blueprint architecture, JSON-based persistence, and Jinja2 Template Inheritance in a scalable structure.

---

📸 Preview
![App Screenshot](https://github.com/hassanimohammadreza/url-shortener/blob/3c5255b3404853f1785629346a01745fc2fa5df4/static/url-shortener.png?raw=true)

---

## 🏗 Project Architecture

```text
📦 project
 ┣ 📂 app
 ┃ ┣ 📜 __init__.py
 ┃ ┗ 📜 routes.py
 ┣ 📂 static
 ┃ ┣ 📂 css
 ┃ ┃ ┗ 📜 style.css
 ┃ ┗ 📂 js
 ┃   ┗ 📜 main.js
 ┣ 📂 templates
 ┃ ┣ 📜 base.html
 ┃ ┗ 📜 index.html
 ┣ 📂 venv
 ┣ 📜 run.py
 ┣ 📜 tasks.json
 ┗ 📜 README.md
```

---

## 🧠 Architecture Overview

### 🔹 Blueprint-Based Modular Design

The application is structured using **Flask Blueprints** to ensure clean separation of concerns and modular development.

```python
main = Blueprint('main', __name__)
```
This makes the application:

- Scalable

- Maintainable

- Easy to extend (authentication, API, admin panel)

- Production-ready structure


### 🔹 JSON-Based Persistence

Tasks are stored in:
```pgsql
tasks.json
```

Each task follows this structure:
```json
{
  "name": "Build Flask App",
  "done": false
}
```

Helper functions:

- `load_tasks()` → Reads tasks from file

- `save_tasks(tasks)` → Saves tasks using formatted JSON

This keeps the project lightweight and easy to migrate later to a database like SQLite or PostgreSQL.

### 🔹 Template Inheritance (Jinja2)

The UI uses template inheritance:
```html
{% extends "base.html" %}
{% block content %}
```

Benefits:

- Reusable layout

- Cleaner HTML structure

- Better maintainability

- Easy UI scaling

## ✨ Features

- ➕ Add new tasks

- ✅ Toggle task completion

- 🗑 Delete tasks

- 💾 Persistent JSON storage

- 🔁 Redirect after actions

- 📦 Modular Blueprint architecture

- 🎨 Separated frontend assets (CSS / JS)

---

## 🌐 Application Routes

The following routes handle all task-related operations within the application:

| Method | Route | Description |
|--------|--------|------------|
| GET | `/` | Render the homepage and display all tasks |
| POST | `/add` | Add a new task to the list |
| GET | `/toggle/<int:task_id>` | Toggle the completion status of a task |
| GET | `/delete/<int:task_id>` | Delete a task from the list |

---

Example toggle logic:
```python
if 0 <= task_id < len(tasks):
    tasks[task_id]['done'] = not tasks[task_id]['done']
```
Safe index validation prevents runtime errors.

---

## ⚙️ Design Decisions
Why JSON Instead of Database?

- No external setup required

- Lightweight persistence

- Easy migration to SQLite/PostgreSQL later

- Great for learning file I/O

Why Blueprint?

- Clean code separation

- Scalable architecture

- Production-like structure

---

## 📈 Roadmap

- SQLite integration

- Task editing

- Due dates

- Task categories

- User authentication

- REST API version

- Docker support

- Unit testing

---

## 🛠 Tech Stack

- Python 3

- Flask

- Jinja2

- HTML5

- CSS3

- JavaScript

- JSON

---

## 📚 Learning Outcomes

This project demonstrates:

- Flask Blueprints

- HTTP routing & methods

- Form handling (request)

- Redirect patterns

- File handling in Python

- Template inheritance

- Clean project organization

---

### 📜 License

This project is licensed under the MIT License.

---

### 👨‍💻 Author

Mohammadreza Hassani  
GitHub: `https://github.com/hassanimohammadreza`

