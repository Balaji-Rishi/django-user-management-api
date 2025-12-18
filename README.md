# 📘 Django User Management API

A backend REST API built using **Python & Django** that provides **user registration and login** functionality.  
This project is designed to demonstrate **Django fundamentals, REST API development, database integration, and best practices**.

---

## 🚀 Features

- User Registration API  
- User Login API  
- Password hashing for security  
- RESTful API architecture  
- Django REST Framework  
- MySQL database integration  
- Django migrations  
- Ready for JWT authentication extension  

---

## 🛠 Tech Stack

- **Language:** Python  
- **Framework:** Django, Django REST Framework  
- **Database:** MySQL  
- **ORM:** Django ORM  
- **Tools:** VS Code, Postman, Git  
- **Version Control:** Git & GitHub  

---

## 📁 Project Structure

django_user_project/
│
├── config/
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
│
├── users/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── urls.py
│
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md

yaml
Copy code

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/django-user-management-api.git
cd django-user-management-api
2️⃣ Create & activate virtual environment
bash
Copy code
python -m venv venv
Windows

bash
Copy code
venv\Scripts\activate
Mac / Linux

bash
Copy code
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Database Configuration (MySQL)
Create database:

sql
Copy code
CREATE DATABASE django_db;
Update config/settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5️⃣ Apply migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
6️⃣ Run the server
bash
Copy code
python manage.py runserver
Server runs at:

cpp
Copy code
http://127.0.0.1:8000/
🔗 API Endpoints
🔹 Register User
arduino
Copy code
POST /api/register/
Request Body

json
Copy code
{
  "username": "Balaji",
  "password": "Balaji@1"
}
Response

json
Copy code
{
  "message": "User registered"
}
🔹 Login User
bash
Copy code
POST /api/login/
Request Body

json
Copy code
{
  "username": "Balaji",
  "password": "Balaji@1"
}
Response

json
Copy code
{
  "message": "Login successful"
}
🧪 API Testing
Swagger (optional)

Postman (recommended for real-time testing)

Steps:

Open Postman

Select POST request

Use API URL

Add JSON body

Send request

🔐 Security
Passwords are hashed using Django’s built-in hashing system

Plain text passwords are never stored

Ready to extend with JWT authentication

📌 Future Enhancements
JWT Authentication

Role-based access control

Refresh tokens

Docker support

Deployment on AWS / Render

👨‍💻 Author
Balaji
Java Full Stack Developer | Python Backend Developer
GitHub: https://github.com/YOUR_USERNAME

📄 License
This project is open-source and available for learning and educational purposes.

Run these commands:

```bash
git add README.md
git commit -m "Add detailed project README"
git push
