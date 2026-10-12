# 🔐 Cloud Authentication & Privacy Project

A **cloud-based authentication and privacy management web application** developed using **Python, Django, and SQLite**. The project demonstrates secure user authentication, database management, privacy-focused application design, and the fundamentals of deploying a Python web application in a cloud environment.      

## 📌 Project Overview

This project was developed to demonstrate how a **Django-based web application** can manage user authentication and application data while maintaining a structured and privacy-oriented architecture.

The application uses **Django** as the backend framework and **SQLite** for database management. It is designed with separate application and project components to maintain a clean and scalable project structure.

## 🚀 Key Features

- 🔐 **User Authentication**
  - User registration
  - User login and logout.    
  - Session-based authentication
  - Protected application pages

- 🛡️ **Privacy Management**
  - Privacy-focused application design
  - Controlled access to application resources
  - Separation of application and database components

- 🗄️ **Database Management**
  - SQLite database integration
  - Structured storage of application and user information
  - Django ORM for database operations

- 🌐 **Cloud-Ready Architecture**
  - Python/Django web application
  - Suitable for deployment on cloud infrastructure
  - Can be hosted on platforms such as AWS EC2

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Backend programming |
| **Django** | Web application framework |
| **SQLite** | Database |
| **HTML/CSS** | Frontend |
| **Django ORM** | Database operations |
| **Git & GitHub** | Version control |
| **Linux** | Server/deployment environment |
| **AWS** | Cloud deployment |

## 📂 Project Structure

```text
cloud_auth_project/
│
├── database/
│   └── Database-related files
│
├── privacy_app/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
│
├── privacy_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── ...
│
├── manage.py
├── db.sqlite3
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shibisaran/cloud_auth_project.git
```

```bash
cd cloud_auth_project
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django
```

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 6. Start the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## 🔑 Authentication Flow

The basic authentication workflow is:

```text
User
  │
  ▼
Registration / Login
  │
  ▼
Django Authentication
  │
  ▼
Session Validation
  │
  ▼
Protected Application
  │
  ▼
Database
```

Unauthenticated users are restricted from accessing protected resources, while authenticated users can access the application's authorized functionality.

## 🗄️ Database

The project uses **SQLite** as the database.

Django's ORM provides an abstraction layer between the application and database:

```text
Django Application
        │
        ▼
    Django ORM
        │
        ▼
      SQLite
```

This makes it easier to create, retrieve, update, and delete application data without writing raw SQL for every operation.


## 🔒 Security Considerations

For production deployment, the following security practices should be implemented:

- Store Django `SECRET_KEY` securely.
- Never commit passwords or credentials to GitHub.
- Set `DEBUG = False` in production.
- Configure `ALLOWED_HOSTS`.
- Use HTTPS.
- Use environment variables for sensitive configuration.
- Apply least-privilege access to cloud resources.
- Keep dependencies updated.
- Restrict unnecessary network ports through AWS Security Groups.
- Use a production database instead of SQLite for high-traffic applications.

## 🧪 Testing

Run Django's test suite using:

```bash
python manage.py test
```

The application can be tested for:

- User registration
- User login/logout
- Authentication restrictions
- Database operations
- Protected pages
- Invalid login attempts
- Application access control

## 📈 Future Enhancements

The project can be further enhanced with:

- 🔑 Password reset functionality
- 📧 Email verification
- 🔐 Multi-factor authentication
- 🛡️ Role-based access control
- 🔒 HTTPS/SSL configuration
- ☁️ AWS deployment
- 🗄️ Amazon RDS integration
- 📦 Docker containerization
- 🔄 CI/CD using GitHub Actions
- 📊 CloudWatch monitoring
- 🚨 CloudWatch alarms and notifications
- 🌍 Cloudflare DNS and security
- 🔎 Application logging and auditing

## 🎯 Learning Outcomes

Through this project, the following concepts were practiced:

- **Python web development**
- **Django architecture**
- **MVC/MVT application structure**
- **User authentication**
- **Database management**
- **Django ORM**
- **Git and GitHub**
- **Linux application deployment**
- **Cloud deployment concepts**
- **Application security and privacy**

## 👨‍💻 Author

**Shibisaran M**

- GitHub: [Shibisaran](https://github.com/Shibisaran)
- 
⭐ If you find this project useful, consider giving the repository a star.
