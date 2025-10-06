````markdown
# E-commerce API with FastAPI

Ye ek backend project hai jo **FastAPI** ke upar bana hai. Iska purpose hai ek simple e-commerce system ke liye API provide karna jisme user authentication, product management, aur email notifications included hain.

---

## 🚀 Features

- User signup & login (JWT authentication)
- Secure password hashing
- CRUD operations for Products
- User profile management
- Email verification & password reset
- Token-based authentication
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

Project ke root me ek `.env` file banao aur ye variables set karo:

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

(Production ke liye PostgreSQL ka URL use karna recommended hai.)

### 5. Run Application

```bash
uvicorn main:app --reload
```

Server `http://127.0.0.1:8000` par run hoga.
Swagger docs: `http://127.0.0.1:8000/docs`
Redoc: `http://127.0.0.1:8000/redoc`

---

## 📌 API Endpoints

| Method | Endpoint                  | Description                 | Auth Required |
| ------ | ------------------------- | --------------------------- | ------------- |
| POST   | `/auth/signup`            | User registration           | ❌             |
| POST   | `/auth/login`             | User login, token return    | ❌             |
| GET    | `/users/me`               | Current user profile        | ✅             |
| POST   | `/password-reset`         | Send password reset email   | ❌             |
| POST   | `/password-reset/confirm` | Confirm password reset      | ❌             |
| GET    | `/products/`              | List all products           | ❌             |
| GET    | `/products/{id}`          | Get product detail          | ❌             |
| POST   | `/products/`              | Create product (Admin only) | ✅             |
| PUT    | `/products/{id}`          | Update product (Admin only) | ✅             |
| DELETE | `/products/{id}`          | Delete product (Admin only) | ✅             |

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

Agar tests likhe gaye hain to run karo:

```bash
pytest
```

---

## 🤝 Contributing

Contributions welcome hain!

1. Fork repo
2. Branch banao (`git checkout -b feature/xyz`)
3. Changes commit karo
4. Pull request bhejo

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
...
```
