````markdown
<h1 align="center">🛒 E-commerce API with FastAPI</h1>

<p align="center">
A backend project built with <b>FastAPI</b> that provides RESTful APIs for an e-commerce system.  
Includes <b>user authentication, product management, and email notifications</b>.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" />
  <img src="https://img.shields.io/badge/FastAPI-Framework-brightgreen.svg" />
  <img src="https://img.shields.io/badge/Database-PostgreSQL%2FSQLite-orange.svg" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" />
</p>

---

## 🚀 Features

✅ User signup & login with JWT authentication  
✅ Secure password hashing  
✅ CRUD operations for Products  
✅ User profile management  
✅ Email verification & password reset  
✅ Role-based access (admin/user)  
✅ Input validation & error handling  

---

## 🛠️ Tech Stack

- ⚡ **FastAPI** – High performance web framework  
- 📦 **Pydantic** – Data validation  
- 🗄️ **SQLAlchemy** – ORM for database  
- 🐘 **PostgreSQL / SQLite** – Database  
- 🔐 **JWT / OAuth2** – Authentication  
- 📧 **SMTP / Jinja2** – Email notifications  
- 🚀 **Uvicorn** – ASGI server  

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

Create a `.env` file in the project root:

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

Server → `http://127.0.0.1:8000`
Swagger UI → `http://127.0.0.1:8000/docs`
Redoc → `http://127.0.0.1:8000/redoc`

---

## 📌 API Endpoints

| Method   | Endpoint                  | Description                 | Auth |
| -------- | ------------------------- | --------------------------- | ---- |
| `POST`   | `/auth/signup`            | Register a new user         | ❌    |
| `POST`   | `/auth/login`             | Login & get token           | ❌    |
| `GET`    | `/users/me`               | Get current user profile    | ✅    |
| `POST`   | `/password-reset`         | Send password reset email   | ❌    |
| `POST`   | `/password-reset/confirm` | Confirm password reset      | ❌    |
| `GET`    | `/products/`              | List all products           | ❌    |
| `GET`    | `/products/{id}`          | Get product details         | ❌    |
| `POST`   | `/products/`              | Create product (Admin only) | ✅    |
| `PUT`    | `/products/{id}`          | Update product (Admin only) | ✅    |
| `DELETE` | `/products/{id}`          | Delete product (Admin only) | ✅    |

---

## 📂 Project Structure

```
.
├── main.py             # Entry point
├── models.py           # Database models
├── routers/            # All API routes
├── schemas/            # Pydantic schemas
├── templates/          # Email templates
├── emails.py           # Email logic
├── requirements.txt    # Dependencies
├── .env.example        # Env variables
└── README.md           # Documentation
```

---

## ✅ Testing

```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch (`git checkout -b feature/xyz`)
3. Commit changes
4. Push to branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

<p align="center">Made with ❤️ using FastAPI</p>
```
