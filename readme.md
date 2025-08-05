Absolutely! Here's a **complete `README.md` content** based on everything we’ve built so far:

---

# 🧩 Django REST API – JWT Auth with RBAC

A Django project with:

* JWT-based Authentication (via Simple JWT)
* Role-Based Access Control (Buyer, Seller, Admin)
* Custom User Model
* Auth APIs (Register, Login, Profile, Change Password)
* Protected endpoints by role

---

## 📁 Project Structure

```
myproject/
├── accounts/            # App for user accounts and auth
│   ├── models.py        # Custom User model with roles
│   ├── views.py         # Auth views
│   ├── serializers.py   # DRF serializers
│   ├── permissions.py   # Role-based access control
│   └── urls.py
├── myproject/
│   ├── settings.py      # App & JWT config
│   └── urls.py
├── manage.py
```

---

## ⚙️ Setup Instructions

### 🧱 1. Clone and Navigate

```bash
git clone <repo-url>
cd myproject
```

---

### 🧪 2. Create Virtual Environment

```bash
python3 -m venv env
source env/bin/activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Or manually:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

---

### 🛠 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 🚀 5. Run Development Server

```bash
python manage.py runserver
```

Now open:
👉 `http://127.0.0.1:8000`

---

## 🔐 JWT Authentication

### 🔑 Generate Token

Use `POST /api/auth/login/` to get:

* Access token
* Refresh token

Use access token in headers:

```
Authorization: Bearer <access_token>
```

---

## 🔄 Roles and Access

| Role   | Description               |
| ------ | ------------------------- |
| Buyer  | Can access buyer routes   |
| Seller | Can access seller routes  |
| Admin  | Full control (extendable) |

---

## 📜 API Endpoints

| API Endpoint                 | Method | Auth Required | Role Needed | Description                                |
| ---------------------------- | ------ | ------------- | ----------- | ------------------------------------------ |
| `/api/auth/register/`        | POST   | ❌             | None        | Register with username/email/password/role |
| `/api/auth/login/`           | POST   | ❌             | None        | Login and get JWT tokens                   |
| `/api/auth/profile/`         | GET    | ✅             | Any         | Get current logged-in user info            |
| `/api/auth/change-password/` | POST   | ✅             | Any         | Change password                            |
| `/api/buyer-only/`           | GET    | ✅             | Buyer       | Buyer-only route                           |


### 🔓 Public Endpoints

| Method | URL                   | Description             |
| ------ | --------------------- | ----------------------- |
| POST   | `/api/auth/register/` | Register user with role |
| POST   | `/api/auth/login/`    | Login & get JWT tokens  |

---

### 🔐 Authenticated Endpoints (All Roles)

| Method | URL                          | Description                |
| ------ | ---------------------------- | -------------------------- |
| GET    | `/api/auth/profile/`         | Get logged-in user profile |
| POST   | `/api/auth/change-password/` | Change password            |

---

### 🎯 Role-Based Protected Endpoint

| Method | URL                | Role Required | Description       |
| ------ | ------------------ | ------------- | ----------------- |
| GET    | `/api/buyer-only/` | Buyer         | Buyer-only access |

---

## 🔍 Postman Testing Instructions

1. Register 3 users (Buyer, Seller, Admin) via `/register/`
2. Login each one to get `access` token
3. Use that token in **Authorization → Bearer Token**
4. Access `/profile/`, `/change-password/`, and role-restricted routes like `/buyer-only/`

---

## 🛠 Environment Variables

No `.env` yet. Add `.env` support if needed for secrets.

---

## ✅ TODO (Next Steps)

* [ ] Add forgot/reset password with OTP or email
* [ ] Add refresh token endpoint
* [ ] Setup Swagger or ReDoc API docs
* [ ] Add seller-only and admin-only routes
* [ ] Add email verification

---

Would you like me to generate this as a downloadable `README.md` file too?
