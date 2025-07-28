# Credit Approval API

This Django RESTful API allows registering customers and determining approved credit limits.

---

##  Setup Instructions

### 1. Clone the repository (if applicable)
```bash
git clone <your-repo-url >
cd credit-approval

# Credit Approval System 💳

A Django REST API for customer registration and credit approval using income-based loan eligibility logic. Dockerized for easy setup and deployment.

---

## 🚀 Features

- Register a new customer
- Automatically calculate credit approved limit based on income
- PostgreSQL database integration
- Fully Dockerized backend using Docker Compose

---

## 📦 Tech Stack

- Python 3.10
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose

---

## ⚙️ Local Setup Instructions

Make sure you have **Docker Desktop** installed.

```bash
git clone https://github.com/YOUR_USERNAME/credit-approval.git
cd credit-approval
docker-compose up --build
