[README-3.md](https://github.com/user-attachments/files/28670235/README-3.md)
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=E8621A,1a1a1a&height=200&section=header&text=Restaurant%20Management&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Full-stack%20Django%20web%20platform%20for%20restaurant%20operations&descAlignY=58&descSize=16" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.8+-FFD43B?style=for-the-badge&logo=python&logoColor=306998)](https://python.org)
[![Django](https://img.shields.io/badge/Django-6.0.2-092E20?style=for-the-badge&logo=django&logoColor=44B78B)](https://djangoproject.com)
[![MySQL](https://img.shields.io/badge/MySQL-9.0-00758F?style=for-the-badge&logo=mysql&logoColor=white)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-E8621A?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-3ecf8e?style=for-the-badge)]()

<br/>

> *One platform. Every department. Zero chaos.*

<br/>

</div>

---

<div align="center">

## ⟡ What is this?

</div>

A **full-stack restaurant management system** built with Django and MySQL, designed to unify every operation of a restaurant under one roof — from the moment a customer browses the menu to the moment the delivery goes out the door and the books are balanced.

Managers get a live dashboard. Staff get module-specific views. Customers get a clean self-service portal. Everyone stays in their lane thanks to role-based access control.

---

<div align="center">

## 🧩 Modules

</div>

<div align="center">

| &nbsp; | Module | What it does |
|:---:|:---|:---|
| 📊 | **Dashboard** | Live KPIs, activity feed, and quick navigation for managers |
| 🛒 | **Orders** | Create, list, detail, and track dine-in or take-away orders |
| 🍽️ | **Products** | Full menu catalogue — add dishes, set prices, upload photos |
| 📦 | **Inventory** | Ingredient stock tracking with automatic low-level alerts |
| 🚴 | **Delivery** | Delivery order queue and driver assignment |
| 💰 | **Finance** | Revenue summaries, expense tracking, financial dashboard |
| 👥 | **HR** | Staff directory, roles, scheduling, and employee records |
| 🧑‍💻 | **Customer** | Self-service portal — browse menu, place order, get confirmation |
| 🔐 | **Users** | Login, registration, role-based decorators, and access control |

</div>

---

<div align="center">

## 🏗️ Tech Stack

</div>

<div align="center">

|  | Technology | Version | Role |
|:---:|:---|:---:|:---|
| 🐍 | **Python** | 3.8+ | Runtime |
| 🎸 | **Django** | 6.0.2 | Web framework |
| 🗄️ | **MySQL** | 9.0 | Relational database |
| 🔌 | **mysql-connector-python** | 9.0.0 | DB driver |
| 🔑 | **python-dotenv** | 1.0.0 | Environment config |
| 🎨 | **HTML / CSS / JS** | — | Frontend templates |

</div>

---

<div align="center">

## 🗂️ Project Structure

</div>

```
📁 Restaurant-Management-Apps/
│
├── 📄 manage.py
├── 🔒 .env                        ← secrets — never commit this
├── 📄 requirements.txt
├── 🗃️  Base_Restaurant.sql         ← full schema + seed data
│
├── 📁 restaurant_project/          ← Django core
│   ├── settings.py
│   ├── urls.py  ·  views.py
│   └── wsgi.py  ·  asgi.py
│
├── 📁 dashboard/    📁 orders/     📁 products/
├── 📁 inventory/    📁 delivery/   📁 finance/
├── 📁 hr/           📁 customer/   📁 users/
│   └── admin.py · apps.py · models.py · views.py · urls.py
│
├── 📁 templates/
│   ├── base.html  ·  customer_base.html  ·  welcome.html
│   └── [one sub-folder per module]
│
└── 📁 static/
    ├── css/style.css
    ├── img/          ← logo, login banner, product photos
    └── js/
```

---

<div align="center">

## 🚀 Getting Started

</div>

### Prerequisites

Before anything, make sure you have:

- ✅ **Python 3.8+** — [python.org](https://python.org)
- ✅ **MySQL** running locally — [mysql.com](https://mysql.com)
- ✅ **pip** (comes with Python)

---

### Installation

**① Clone the repo**

```bash
git clone https://github.com/your-username/Restaurant-Management-Apps.git
cd Restaurant-Management-Apps
```

---

**② Create & activate a virtual environment**

```bash
# 🪟 Windows
python -m venv venv
venv\Scripts\activate

# 🍎 macOS / 🐧 Linux
python3 -m venv venv
source venv/bin/activate
```

---

**③ Install dependencies**

```bash
pip install -r requirements.txt
```

---

**④ Create the database & import the seed**

```sql
-- In your MySQL shell:
CREATE DATABASE restaurant_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

```bash
# Back in your terminal:
mysql -u root -p restaurant_db < Base_Restaurant.sql
```

---

**⑤ Set up your `.env` file**

Create a file named `.env` at the project root and fill it in:

```env
SECRET_KEY=your-django-secret-key-here
DEBUG=True

DB_NAME=restaurant_db
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

> 💡 Generate a secret key instantly:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

---

**⑥ Migrate & run**

```bash
python manage.py migrate
python manage.py runserver
```

🎉 Open **http://127.0.0.1:8000** — you're live.

---

<div align="center">

## 🔑 Environment Variables

</div>

| Variable | Default | Description |
|:---|:---:|:---|
| `SECRET_KEY` | — | Django cryptographic key — **required** |
| `DEBUG` | `True` | Set to `False` in production |
| `DB_NAME` | `restaurant_db` | Name of your MySQL database |
| `DB_USER` | `root` | MySQL username |
| `DB_PASSWORD` | — | MySQL password |
| `DB_HOST` | `127.0.0.1` | MySQL host address |
| `DB_PORT` | `3306` | MySQL port |

> ⚠️ **Never push `.env` to GitHub.** It is already listed in `.gitignore`.

---

<div align="center">

## 🛠️ Troubleshooting

</div>

<details>
<summary><b>🔴 SSL error when connecting to MySQL</b></summary>

<br/>

Add this to the `DATABASES` config in `settings.py`:

```python
'OPTIONS': {
    'ssl_disabled': True
}
```

</details>

<details>
<summary><b>🔴 <code>python</code> command not found on Windows</b></summary>

<br/>

Either add Python to your system PATH, or use `py` instead of `python` in every command.

</details>

<details>
<summary><b>🔴 Migrations fail with <code>Access denied</code></b></summary>

<br/>

Double-check `DB_USER` and `DB_PASSWORD` in your `.env`. Make sure that MySQL user has full privileges on the database:

```sql
GRANT ALL PRIVILEGES ON restaurant_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

</details>

<details>
<summary><b>🔴 Static files not loading</b></summary>

<br/>

Run the following to collect static files:

```bash
python manage.py collectstatic
```

</details>

---

<div align="center">

## 📸 Product Images

</div>

Product photos are served from `static/img/products/`. To add a new dish image, drop the file there — no code changes needed.

The following images ship with the project:

| File | Dish |
|:---|:---|
| `Ndole.PNG` | Ndolé |
| `Poulet DG.PNG` | Poulet DG |
| `Riz saute.PNG` | Riz sauté |
| `Jus de Bissap.PNG` | Jus de Bissap |
| `Jus de Jingembre.PNG` | Jus de Gingembre |

---

<div align="center">

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=E8621A,1a1a1a&height=100&section=footer" width="100%"/>

*Built with 🍊 Django · MySQL · Python*

</div>
