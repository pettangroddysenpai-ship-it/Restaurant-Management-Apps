# 🍽️ Restaurant Management Web Application

> **PKFIE Python Course Project** — A full-featured Django-based Restaurant Management System designed to ease and digitize daily restaurant operations.

---

## 📋 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Team](#project-team)
- [Development Timeline](#development-timeline)
- [Results & Metrics](#results--metrics)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

---

## 🧩 About the Project

A web-based system designed to **simplify and streamline daily restaurant operations** — from order management to real-time analytics. This application replaces manual, paper-based restaurant systems with a unified digital platform.

It covers a wide range of restaurant services:

- 🛒 Order Tracking & Management
- 🚚 Delivery & Transport Logistics
- 📅 Reservations
- 👥 Employee & User Management
- 📊 Dashboard Analytics
- 🔐 Staff Authentication & Role-Based Access

> The project was implemented in **8 development phases**, combining UI/UX simulation and full-stack development.

---

## ✨ Features

| Module | Description |
|---|---|
| 🏠 **Dashboard** | Real-time analytics — revenue, popular items, staff performance |
| 🛒 **Orders** | Create, track, and review full order history |
| 🚚 **Delivery** | Track deliveries and manage delivery logistics |
| 📦 **Inventory** | Monitor stock levels, ingredients, and supplies |
| 🍕 **Products** | Manage menu items, categories, and pricing |
| 💰 **Finance** | Monitor revenue, expenses, and financial summaries |
| 👥 **HR** | Manage staff records, roles, and schedules |
| 👤 **Users** | Secure login with role-based access (Admin, Manager, Staff) |
| 📱 **Responsive Design** | Works seamlessly on desktop, tablet, and mobile |

---

## 📁 Project Structure

```
Restaurant-Management-App/
│
├── dashboard/              # Dashboard app — real-time analytics
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── delivery/               # Delivery tracking and logistics
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── finance/                # Financial management
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── hr/                     # Human resources management
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── inventory/              # Inventory and stock management
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── orders/                 # Order management
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── create.html
│   ├── list.html
│   └── urls.py
│
├── products/               # Menu and product management
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── users/                  # User authentication and management
│   ├── migrations/
│   ├── models.py
│   ├── login.html
│   └── urls.py
│
├── restaurant_project/     # Django project configuration
│   ├── users/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── Reports/                # Project reports and documentation
│   ├── Report 1.docx
│   ├── Report 1.pdf
│   └── Restaurant_App_Guide.docx
│
├── Base_Restaurant.sql     # SQL database dump
├── decorators.py           # Custom access/permission decorators
├── manage.py               # Django management script
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | HTML5, CSS3, Django Templates | Page structure, styling, dynamic rendering |
| **Backend** | Python 3.10, Django 4.2 | Server-side logic, database, authentication |
| **Database** | PostgreSQL | Persistent storage for orders, users, menu |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Git
- PostgreSQL

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/restaurant-management-app.git
   cd restaurant-management-app
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment settings**

   Update `restaurant_project/settings.py` with your database credentials and secret key.

---

## 🗄️ Database Setup

To use the provided SQL dump:

```bash
psql -U your_user -d your_database < Base_Restaurant.sql
```

Then apply Django migrations:

```bash
python manage.py migrate
```

Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

---

## ▶️ Usage

Start the development server:

```bash
python manage.py runserver
```

Open in your browser: `http://127.0.0.1:8000`

- **Admin panel:** `http://127.0.0.1:8000/admin/`
- **Login page:** `http://127.0.0.1:8000/users/login/`

---

## 👨‍💻 Project Team

| Role | Count |
|---|---|
| Backend Developers | 2 |
| Frontend Developer | 1 |
| UI/UX Designer | 1 |

---

## 📅 Development Timeline

The project was delivered in **8 phases** across an 8-week period:

| Phase | Duration |
|---|---|
| Simulation (UI/UX Design) | 3 weeks |
| Development | 5 weeks |

---

## 📊 Results & Metrics

- ✅ Final product matched **92%** of original design prototypes
- ⭐ User Acceptance Testing (UAT) scored **4.8 / 5** from restaurant staff

---

## 🗺️ Roadmap

Phase 1 (current) covers core restaurant operations. **Phase 2** will include:

- [ ] 💳 Payment gateway integration
- [ ] 📦 Advanced inventory management
- [ ] 🎁 Customer loyalty programs

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

> Built with ❤️ as part of the **PKFIE Python Course** — a complete digital solution for modern restaurant management.
