````markdown
# E-commerce API with FastAPI

This is a backend project built with **FastAPI** that provides a RESTful API for an e-commerce system.  
It includes features like user authentication, product management, and email notifications.

---

## 🚀 Features

- User signup & login with JWT authentication  
- Secure password hashing  
- CRUD operations for Products  
- User profile management  
- Email verification & password reset  
- Role-based access (admin/user)  
- Input validation & error handling  

---

## 🛠️ Technologies

- [FastAPI](https://fastapi.tiangolo.com/) – Web framework  
- [Pydantic](https://docs.pydantic.dev/) – Data validation  
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database  
- [PostgreSQL / SQLite] – Database (configurable)  
- [JWT / OAuth2] – Authentication  
- [SMTP / Email] – Email notifications  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/msakhawatali/E-commerce-API-with-FastAPI.git
cd E-commerce-API-with-FastAPI
````

### 2. Create Virtual Environment

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root and configure your variables:

```env
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=60

SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASSWORD=your_password
EMAIL_FROM=your_email@example.com

DATABASE_URL=sqlite:///./app.db
```

(Use PostgreSQL for production.)

### 5. Run Application

```bash
uvicorn main:app --reload
```

Server will run at: `http://127.0.0.1:8000`

* Swagger UI: `http://127.0.0.1:8000/docs`
* Redoc: `http://127.0.0.1:8000/redoc`

---

## 📌 API Endpoints

| Method | Endpoint                  | Description                 | Auth Required |
| ------ | ------------------------- | --------------------------- | ------------- |
| POST   | `/auth/signup`            | Register a new user         | No            |
| POST   | `/auth/login`             | Login and get tokens        | No            |
| GET    | `/users/me`               | Get current user profile    | Yes           |
| POST   | `/password-reset`         | Send password reset email   | No            |
| POST   | `/password-reset/confirm` | Confirm password reset      | No            |
| GET    | `/products/`              | List all products           | No            |
| GET    | `/products/{id}`          | Get product details         | No            |
| POST   | `/products/`              | Create product (Admin only) | Yes           |
| PUT    | `/products/{id}`          | Update product (Admin only) | Yes           |
| DELETE | `/products/{id}`          | Delete product (Admin only) | Yes           |

---

## 📂 Project Structure

```
.
├── main.py             # Application entry point
├── models.py           # Database models
├── routers/            # All API routes
├── schemas/            # Pydantic schemas
├── templates/          # Email templates
├── emails.py           # Email handling logic
├── requirements.txt    # Project dependencies
├── .env.example        # Example environment variables
└── README.md           # Documentation
```

---

## ✅ Testing

If tests are included, run them with:

```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/xyz`)
3. Commit your changes
4. Push the branch
5. Submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
...
```

```
```
