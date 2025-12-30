# 🔐 User Authentication API with JWT (FastAPI)

## 📌 Assignment #1

This project implements a **secure REST API** using **FastAPI** with **JWT-based authentication**.
It provides user **signup**, **login**, and **change password**, **Get Profile**,**Update Profile**,**List all users** functionality with proper password hashing and validation.

---

## 🎯 Objective

To develop a secure authentication system that demonstrates:

* 👤 User management
* 🔒 Password hashing using **bcrypt**
* 🪙 JWT token generation and validation
* 🧼 Clean API design and proper error handling

---

## 🛠️ Tech Stack

* ⚡ **Framework:** FastAPI
* 🗄️ **Database:** PostgreSQL
* 🧩 **ORM:** SQLAlchemy
* 🔐 **Password Hashing:** Passlib (bcrypt)
* 🪪 **Authentication:** JWT (python-jose)
* 🔑 **OAuth2:** OAuth2PasswordBearer
* 🚀 **Server:** Uvicorn

---

## 📦 Project Structure

```
app/
├── main.py               # Entry point, initializes FastAPI app and includes routers
├── database.py           # Database connection setup (SQLAlchemy + PostgreSQL)
├── models/
│   └── user.py           # SQLAlchemy User model
├── schemas/
│   └── user.py           # Pydantic schemas for validation (Signup, Login, Change Password,get profile,update profile,list all users)
├── routers/
│   └── auth.py
    └── dependencies.py
    └── users.py      # API routes: signup, login, change-password
└── core/
    └── security.py
    └── config.py      # JWT token generation, password hashing and verification
```
---


## 📊 Database Schema (users table)

| Column Name | Data Type | Constraints                 |
| ----------- | --------- | --------------------------- |
| id          | Integer   | Primary Key, Auto Increment |
| firstname   | String    | Not Null                    |
| lastname    | String    | Not Null                    |
| email       | String    | Unique, Not Null            |
| password    | String    | Hashed, Not Null            |
| createdat   | Timestamp | Default: Current Timestamp  |

---

## 🔐 Security Features

* 🔑 Passwords are **hashed using bcrypt**
* 🪙 JWT tokens are **securely generated and signed**
* 📧 Email uniqueness enforced at database level
* ❗ Proper input validation and error handling
* 🚫 No sensitive data (passwords, secret keys) stored in plain text

---

## 🗂️ File Details

### **1️⃣ main.py**

* Initializes FastAPI app
* Includes routers (app.include_router(auth.router, prefix="/auth"))


### **2️⃣ database.py**

* Creates database engine
* Creates session for CRUD operations
* Connects SQLAlchemy with PostgreSQL

### **3️⃣ models/user.py**

* Defines User table using SQLAlchemy ORM
* Fields: id, firstname, lastname, email, password, createdat

### **4️⃣ schemas/user.py**

* Defines Pydantic models for request validation
* Models:

  * SignupSchema → firstname, lastname, email, password
  * LoginSchema → email, password
  * ChangePasswordSchema → email, old_password, new_password

### **5️⃣ routers/auth.py**

* Contains API endpoints:

  * **POST /auth/signup** → Create user
  * **POST /auth/login** → Login user and return JWT token
  * **POST /auth/change-password** → Change password
* Handles all input validation and error responses

### **6️⃣ core/security.py/config.py**

* Password hashing using **bcrypt**
* Verify password
* JWT token generation and decoding
* Token expiry handling

---

## 📬 Example API Requests

### ➤ Signup

**POST** /auth/signup

json
{
  "firstname": "Bisma",
  "lastname": "Mirza",
  "email": "bisma@example.com",
  "password": "password123"
}

---

### ➤ Login

**POST** /auth/login

json
{
  "email": "bisma@example.com",
  "password": "password123"
}

**Response**

json
{
  "message": "Login successful",
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}

---

### ➤ Change Password

**POST** /auth/change-password

json
{
  "email": "bisma@example.com",
  "old_password": "password123",
  "new_password": "newpassword456"
}

## 🪙 JWT Token Payload Example

json
{
  "user_id": 1,
  "email": "bisma@example.com",
  "exp": 1735555200  # 30 mints
}

--- 
