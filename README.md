<div align="center">

# 📝 Todo App - FastAPI

### A Modern, Production-Ready RESTful API

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.119.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)

[Live Demo](https://todoapp-fastapi-2zwu.onrender.com/docs) • [Documentation](https://todoapp-fastapi-2zwu.onrender.com/redoc) • [Report Bug](https://github.com/Prashant-Baral/TodoApp_FastAPI/issues)

</div>

---

## ✨ About The Project

A full-featured, production-ready RESTful API for managing todos with robust user authentication, built using modern Python technologies. This project demonstrates industry best practices in API development, database management, and secure authentication.

> **📚 Learning Project**: Developed as part of [Eric Roby's comprehensive FastAPI course](https://www.udemy.com/course/fastapi-the-complete-course/) on Udemy, showcasing real-world application development from concept to deployment.

### 🎯 Key Highlights

- 🔐 **Secure Authentication** - JWT-based auth with bcrypt password hashing
- 📊 **RESTful Design** - Clean, intuitive API endpoints
- 🗄️ **Database Flexibility** - PostgreSQL for production, SQLite for development
- 🔄 **Database Migrations** - Seamless schema changes with Alembic
- 📖 **Auto Documentation** - Interactive Swagger UI and ReDoc
- ✅ **Testing Suite** - Comprehensive test coverage with pytest
- 🚀 **Production Ready** - Deployed and running on Render

---

## 🚀 Features

<table>
<tr>
<td width="50%">

### 👤 User Management
- ✅ User registration with validation
- ✅ Secure login with JWT tokens
- ✅ Password change functionality
- ✅ User profile management
- ✅ Role-based access control

</td>
<td width="50%">

### 📋 Todo Operations
- ✅ Create, read, update, delete todos
- ✅ Priority levels and completion status
- ✅ User-specific todo lists
- ✅ Advanced filtering options
- ✅ Pagination support

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ Security
- ✅ JWT authentication
- ✅ Bcrypt password hashing
- ✅ Protected routes
- ✅ Token expiration
- ✅ Secure headers

</td>
<td width="50%">

### 👨‍💼 Admin Features
- ✅ View all todos
- ✅ Delete any todo
- ✅ User management
- ✅ System oversight
- ✅ Advanced permissions

</td>
</tr>
</table>

---

## 🛠️ Built With

<div align="center">

| Technology | Purpose | Version |
|------------|---------|---------|
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) | Web Framework | 0.119.0 |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=flat&logo=sqlalchemy&logoColor=white) | ORM | 2.0.44 |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) | Database | 2.9.11 |
| ![Alembic](https://img.shields.io/badge/Alembic-yellow?style=flat) | Migrations | 1.17.1 |
| ![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=flat) | Validation | 2.12.3 |
| ![Uvicorn](https://img.shields.io/badge/Uvicorn-2C5F2D?style=flat) | ASGI Server | 0.37.0 |
| ![Python-Jose](https://img.shields.io/badge/Python--Jose-blue?style=flat) | JWT | 3.5.0 |
| ![Passlib](https://img.shields.io/badge/Passlib-green?style=flat) | Hashing | 1.7.4 |

</div>

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- ![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
- ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white) (for production)
- ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
- ![pip](https://img.shields.io/badge/pip-latest-3776AB?style=flat&logo=pypi&logoColor=white)

---

## 🚀 Getting Started

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Prashant-Baral/TodoApp_FastAPI.git
   cd TodoApp_FastAPI
   ```

2. **Create and activate virtual environment**
   
   **Windows:**
   ```bash
   python -m venv n_fastapienv
   n_fastapienv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   python -m venv n_fastapienv
   source n_fastapienv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   cd to_do_app
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the `to_do_app` directory:
   ```env
   SECRET_KEY=your-super-secret-key-here
   ALGORITHM=HS256
   DATABASE_URL=sqlite:///./test.db
   ```

5. **Run database migrations**
   ```bash
   alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

7. **Access the API** 🎉
   - API: http://localhost:8000
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

---

## 📚 API Documentation

### Interactive Documentation

Once the server is running, explore the API using:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs) - Interactive API testing
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc) - Beautiful API documentation

### Quick API Reference

<details>
<summary><b>🔐 Authentication Endpoints</b></summary>

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/token` | Login and get access token |

</details>

<details>
<summary><b>📋 Todo Endpoints</b></summary>

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/todos` | Get all todos for user | ✅ |
| `GET` | `/todos/{id}` | Get specific todo | ✅ |
| `POST` | `/todos` | Create new todo | ✅ |
| `PUT` | `/todos/{id}` | Update todo | ✅ |
| `DELETE` | `/todos/{id}` | Delete todo | ✅ |

</details>

<details>
<summary><b>👤 User Endpoints</b></summary>

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/users/me` | Get current user profile | ✅ |
| `PUT` | `/users/password` | Change password | ✅ |

</details>

<details>
<summary><b>👨‍💼 Admin Endpoints</b></summary>

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/admin/todos` | Get all todos (any user) | ✅ Admin |
| `DELETE` | `/admin/todos/{id}` | Delete any todo | ✅ Admin |

</details>

---

## 📁 Project Structure

```
📦 TodoApp_FastAPI
├── 📂 to_do_app/
│   ├── 📂 alembic/              # Database migrations
│   │   └── 📂 versions/         # Migration files
│   ├── 📂 routers/              # API route handlers
│   │   ├── 📄 auth.py          # Authentication logic
│   │   ├── 📄 todos.py         # Todo CRUD operations
│   │   ├── 📄 admin.py         # Admin functionality
│   │   └── 📄 users.py         # User management
│   ├── 📂 static/              # Static files
│   ├── 📂 templates/           # HTML templates
│   ├── 📂 test/                # Test suite
│   ├── 📄 main.py              # Application entry point
│   ├── 📄 models.py            # SQLAlchemy models
│   ├── 📄 database.py          # Database configuration
│   ├── 📄 alembic.ini          # Alembic config
│   └── 📄 requirements.txt     # Dependencies
├── 📄 README.md                # You are here!
├── 📄 .gitignore              # Git ignore rules
└── 📄 LICENSE                  # MIT License
```

---

## 🧪 Running Tests

Execute the test suite with pytest:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=to_do_app
```

---

## 🚀 Deployment

### Deploy to Render

<details>
<summary><b>Click to expand deployment guide</b></summary>

1. **Create a PostgreSQL Database**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "PostgreSQL"
   - Choose free tier
   - Note the database connection details

2. **Create a Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure settings:
     - **Name**: `todoapp-fastapi`
     - **Root Directory**: `to_do_app`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
     - **Pre-Deploy Command**: `alembic upgrade head`

3. **Add Environment Variables**
   ```
   DATABASE_URL = [Your PostgreSQL Internal URL]
   SECRET_KEY = [Generate a secure random key]
   ALGORITHM = HS256
   ```

4. **Deploy!** 🎉
   - Click "Create Web Service"
   - Wait for the build to complete
   - Your API is now live!

</details>

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DATABASE_URL` | Database connection string | ✅ | `sqlite:///./test.db` |
| `SECRET_KEY` | JWT secret key | ✅ | - |
| `ALGORITHM` | JWT algorithm | ✅ | `HS256` |

### Generate Secret Key

```python
import secrets
print(secrets.token_urlsafe(32))
```

---

## 🤝 Contributing

Contributions make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

<div align="center">

### Prashant Baral

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Prashant-Baral)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:prashantbaral09@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/prashant-baral1)

</div>

---

## 🙏 Acknowledgments

<div align="center">

### Special Thanks

**Eric Roby** - For his comprehensive FastAPI course that guided this project

[![Udemy Course](https://img.shields.io/badge/Udemy-FastAPI_Course-A435F0?style=for-the-badge&logo=udemy&logoColor=white)](https://www.udemy.com/course/fastapi-the-complete-course/)

### Built With Amazing Tools

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Render Hosting](https://render.com/)
- All the amazing open-source contributors!

</div>

---

## 📧 Support

<div align="center">

Need help? Have questions?

[![Email](https://img.shields.io/badge/Email-prashantbaral09@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:prashantbaral09@gmail.com)
[![Issues](https://img.shields.io/badge/GitHub-Issues-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Prashant-Baral/TodoApp_FastAPI/issues)

</div>

---

<div align="center">

### ⭐ If you find this project helpful, please give it a star!

**Made with ❤️ and FastAPI**

[⬆ Back to Top](#-todo-app---fastapi)

</div>
