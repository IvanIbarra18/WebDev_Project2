# Django Movie Project

This is a Django-based web application for displaying movies, including data for movies in theaters and on TV. The project includes preloaded data using Django fixtures.

## Team members

- Gilberto Garza
- Mauricio Garza
- Javier Rodriguez
- Jesus Ivan Ibarra

---

## 📦 Setup Instructions

### 1. Clone or extract the project

If using Git:

```
git clone <your-repo-url>
cd WebDev_Project2
```

Or unzip the project and navigate to the root folder.

---

### 2. Navigate to the Django project folder

```
cd Project2
```

---

### 3. Create and activate a virtual environment (optional but recommended)

**Windows:**

```
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**

```
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

### 5. Apply database migrations

```
python manage.py migrate
```

---

### 6. Load initial data (fixtures)

```
python manage.py loaddata app1/fixtures/app1_data.json
```

---

### 7. Run the development server

```
python manage.py runserver
```

Then open your browser at:

```
http://127.0.0.1:8000/
```

---

## ⚠️ Notes

* The database file (`db.sqlite3`) is not included intentionally.
* All required data is loaded using fixtures.
* If images do not appear, ensure static files are correctly configured.

---

## 🛠 Technologies Used

* Django
* HTML / CSS / JavaScript
* SQLite (default Django database)

---

## ✅ Status

Final working version with preloaded data and functional UI components.
