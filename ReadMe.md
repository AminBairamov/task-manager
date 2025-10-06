#  Task Manager API

A full-featured **Task Management Web Application** built with **Flask**, **PostgreSQL**, and **Docker**, deployed to **AWS Elastic Beanstalk**.  
This project provides a secure REST API that allows users to register, log in, and manage their personal tasks with full CRUD functionality.

---

##  Project Overview

The **Task Manager API** allows users to:
- Create an account and log in securely (JWT authentication).
- Manage tasks (Create, Read, Update, Delete).
- Assign priority, status, and due date to each task.
- Filter tasks by status or due date.
- Ensure data privacy — each user can only access their own tasks.

This application demonstrates **backend API design**, **database modeling**, **containerized deployment**, and **cloud deployment** using AWS.

---

##  Technologies Used

| Category | Technology |
|-----------|-------------|
| Backend Framework | Flask (Python) |
| Database | PostgreSQL |
| Authentication | Flask-JWT-Extended |
| Password Hashing | Flask-Bcrypt |
| ORM | Flask-SQLAlchemy |
| Testing | Pytest + pytest-flask |
| Containerization | Docker, Docker Compose |
| Cloud Deployment | AWS Elastic Beanstalk |
| Version Control | Git, GitHub |

---

##  Features

###  User Management
- **Register** new users with unique usernames and emails.
- **Login** with JWT-based authentication.
- **Secure password hashing** using `Flask-Bcrypt`.

###  Task Management
- **Create tasks** with title, description, priority, and due date.
- **View all tasks** (filtered by user).
- **Filter tasks** by status or due date.
- **Edit or delete tasks** individually.
- **Task ownership** ensures users can only see their own tasks.

###  Task Properties
| Field | Description |
|--------|-------------|
| title | Title of the task |
| description | Detailed description |
| priority | `low`, `medium`, or `high` |
| status | `pending`, `in-progress`, or `completed` |
| due_date | Deadline for completion |
| created_at | Automatically generated timestamp |

---

##  Database Design

### **Users Table**
| Column | Type | Details |
|---------|------|----------|
| id | SERIAL | Primary Key |
| username | VARCHAR(50) | Unique, Not Null |
| email | VARCHAR(100) | Unique, Not Null |
| password_hash | TEXT | Hashed password |
| created_at | TIMESTAMP | Default: current time |

### **Tasks Table**
| Column | Type | Details |
|---------|------|----------|
| id | SERIAL | Primary Key |
| user_id | INT | Foreign Key → users.id |
| title | VARCHAR(200) | Not Null |
| description | TEXT | Optional |
| priority | VARCHAR(10) | `low`/`medium`/`high` |
| status | VARCHAR(20) | Default: `pending` |
| due_date | DATE | Optional |
| created_at | TIMESTAMP | Default: current time |

---

##  API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| **POST** | `/users/register` | Register a new user |
| **POST** | `/users/login` | Authenticate user and return JWT |
| **GET** | `/tasks` | Get all tasks (supports filtering) |
| **POST** | `/tasks` | Create a new task |
| **GET** | `/tasks/{id}` | Retrieve a single task |
| **PUT** | `/tasks/{id}` | Update an existing task |
| **DELETE** | `/tasks/{id}` | Delete a task |

###  Example Query

GET /tasks?status=pending&due=2025-09-15


---

##  Testing

Testing is done using `pytest` and `pytest-flask`.

A basic example test (tests/test_basic.py):
def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Task Manager" in response.data

### Docker Setup

1. Build and start containers:
   docker-compose up --build
2. Access the app at:
   http://localhost:5000

### Docker Services
web → Flask application

db → PostgreSQL database

docker-compose.yml automatically creates a volume for persistent data storage.

### AWS Deployment

This app is deployed to AWS Elastic Beanstalk using Docker.
Steps:

1. Initialize Elastic Beanstalk:
   eb init
2. Create environment:
   eb create task-manager-env
3. Deploy:
   eb deploy
4. Open in browser:
   eb open

### Environment Variables

| Variable         | Description                               |
| ---------------- | ----------------------------------------- |
| `FLASK_APP`      | Entry point for Flask (`app`)             |
| `FLASK_ENV`      | Environment mode (development/production) |
| `DATABASE_URL`   | PostgreSQL connection string              |
| `JWT_SECRET_KEY` | Secret key for JWT tokens                 |


### Requirements

Python 3.11+

Docker & Docker Compose

AWS Elastic Beanstalk CLI (eb)

PostgreSQL 15+

Install dependencies locally:
pip install -r requirements.txt

### Challenges & Solutions

| Challenge                      | Solution                                                                 |
| ------------------------------ | ------------------------------------------------------------------------ |
| `502 Bad Gateway` error on AWS | Fixed by adding missing Flask dependencies and rebuilding EB environment |
| Database connection errors     | Corrected `DATABASE_URL` environment variable in docker-compose.yml      |
| Import issues with `pytest`    | Moved `conftest.py` to root and fixed `PYTHONPATH` setup                 |
| Docker build issues            | Updated `Dockerfile` and used lightweight `python:3.11-slim` image       |


### Conclusion

This project demonstrates:

Building and structuring a professional Flask REST API.

Using PostgreSQL with SQLAlchemy ORM.

Implementing JWT authentication.

Writing automated tests.

Deploying a containerized app to AWS Elastic Beanstalk.

It represents a complete, cloud-ready, and testable Python backend solution.


### Author
## Amin Bairamov 
## Email: bajramovamin52@gmail.com
## GitHub: https://github.com/AminBairamov
