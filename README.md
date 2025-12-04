# Todo App - FastAPI

A full-featured RESTful API for managing todos with user authentication, built with FastAPI and SQLAlchemy.

> **Note**: This project was developed as part of Eric Roby's FastAPI course on Udemy, demonstrating best practices in building modern Python web APIs.

## 🚀 Features

- **User Authentication**: Secure JWT-based authentication system
- **Todo Management**: Create, read, update, and delete todos
- **User Management**: User registration and profile management
- **Admin Features**: Administrative controls for managing users and todos
- **Database**: PostgreSQL for production, SQLite for local development
- **Database Migrations**: Alembic for seamless schema changes
- **API Documentation**: Auto-generated interactive API docs with Swagger UI

## 📋 Prerequisites

- Python 3.8 or higher
- PostgreSQL (for production) or SQLite (for local development)
- pip (Python package manager)

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Prashant-Baral/TodoApp_FastAPI.git
cd TodoApp_FastAPI
```

### 2. Create a virtual environment

```bash
python -m venv n_fastapienv
```

### 3. Activate the virtual environment

**Windows:**
```bash
n_fastapienv\Scripts\activate
```

**macOS/Linux:**
```bash
source n_fastapienv/bin/activate
```

### 4. Install dependencies

```bash
cd to_do_app
pip install -r requirements.txt
```

### 5. Set up environment variables

Create a `.env` file in the `to_do_app` directory:

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
DATABASE_URL=sqlite:///./test.db
```

### 6. Run database migrations

```bash
alembic upgrade head
```

### 7. Start the development server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🗂️ Project Structure

```
to_do_app/
├── alembic/              # Database migration files
├── routers/              # API route handlers
│   ├── auth.py          # Authentication endpoints
│   ├── todos.py         # Todo CRUD endpoints
│   ├── admin.py         # Admin endpoints
│   └── users.py         # User management endpoints
├── static/              # Static files
├── templates/           # HTML templates
├── test/                # Test files
├── main.py              # Application entry point
├── models.py            # SQLAlchemy models
├── database.py          # Database configuration
├── alembic.ini          # Alembic configuration
└── requirements.txt     # Project dependencies
```

## 🔑 API Endpoints

### Authentication
- `POST /auth/register` - Register a new user
- `POST /auth/token` - Login and get access token

### Todos
- `GET /todos` - Get all todos for authenticated user
- `GET /todos/{todo_id}` - Get a specific todo
- `POST /todos` - Create a new todo
- `PUT /todos/{todo_id}` - Update a todo
- `DELETE /todos/{todo_id}` - Delete a todo

### Users
- `GET /users/me` - Get current user profile
- `PUT /users/password` - Change user password

### Admin
- `GET /admin/todos` - Get all todos (admin only)
- `DELETE /admin/todos/{todo_id}` - Delete any todo (admin only)

## 🧪 Running Tests

```bash
pytest
```

## 🚀 Deployment

### Deploy to Render

1. **Create a PostgreSQL database** on Render
2. **Create a Web Service** and connect your GitHub repository
3. **Configure the service**:
   - **Root Directory**: `to_do_app`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Pre-Deploy Command**: `alembic upgrade head`
4. **Add Environment Variables**:
   - `DATABASE_URL` - Link to your PostgreSQL database
   - `SECRET_KEY` - Generate a secure secret key
   - `ALGORITHM` - `HS256`

## 🔧 Technology Stack

- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **PostgreSQL** - Production database
- **Pydantic** - Data validation
- **Python-Jose** - JWT token handling
- **Passlib** - Password hashing
- **Uvicorn** - ASGI server

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./test.db` |
| `SECRET_KEY` | Secret key for JWT encoding | Required |
| `ALGORITHM` | JWT algorithm | `HS256` |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Prashant Baral**
- GitHub: [@Prashant-Baral](https://github.com/Prashant-Baral)

## 🙏 Acknowledgments

- **Eric Roby** - This project was built following Eric Roby's comprehensive FastAPI course on Udemy
- Course: [FastAPI - The Complete Course 2024 (Beginner + Advanced)](https://www.udemy.com/course/fastapi-the-complete-course/)
- FastAPI documentation and community
- SQLAlchemy documentation
- All contributors who help improve this project

## 📧 Support

For support, email prashantbaral09@gmail.com or open an issue in the GitHub repository.

---

⭐ If you find this project helpful, please give it a star!
