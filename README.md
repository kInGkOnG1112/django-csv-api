# Django CSV API Project

This is a Django-based RESTful API project that uses a **CSV file** as the primary data source instead of a traditional database like PostgreSQL or SQLite. It is designed for lightweight use cases where the data is static or only updated via the API layer.

## Features

- Exposes API endpoints using Django REST Framework
- Reads from and optionally writes to a CSV file as a "database"
- Lightweight and easy to deploy
- Fully documented using Swagger

---

## 🛠 Project Setup

Follow the steps below to set up the project in your local environment:

### 1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-django-csv-api.git
cd your-django-csv-api
```

### 2. **Install Python**
Ensure you have **Python 3.12+** installed.

You can check your current version using:

```bash
python --version
```

### 3. **Create a virtual environment**
Create and activate a virtual environment to manage dependencies.

**On Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
source venv\Scripts\activate
```

### 4. **Install dependencies**
Install all required packages from requirements.txt:
```bash
pip install -r requirements.txt
```

## 🚀 Running the Project

### **Run the development server**
```bash
python manage.py runserver
```
The API should now be accessible at:
#### `http://127.0.0.1:8000/`

## 📁 CSV Data Structure

The data is stored in `django-csv-api/videos.csv`.

Make sure the CSV file follows the expected column structure, such as:
```bash
id,name,href,post_date,views_count
7473046841,Patrizienta,https://www.tiktok.com/@patrizienta/video/108426800413716480,06/17/2023,6218
9393801739,NailArtVideos,https://www.tiktok.com/@nailsartvideos/video/108795592566304768,08/18/2023,2812
```
The configuration of the CSV path, structure and the code handling of the CSV read/write logic can be found in ``utils/models.py``.

## 📘 API Endpoints

### Videos

#### 📥 GET  
`/api/videos/?sort_by=post_date&order=asc`  
Retrieve all video records.  
Supports optional query parameters:
- `sort_by`: Field to sort by (`name`, `post_date`, `views_count`)
- `order`: Sorting order (`asc` or `desc`)

#### ➕ POST  
`/api/videos/`  
Add a new video record.  

**Request Body:**

```json
{
  "name": "string",
  "href": "string",
  "post_date": "YYYY-MM-DD",
  "views_count": 0
}
```

#### ✏️ PUT
`/api/videos/{id}/`  
Update an existing video record by ID.

**Request Body:**

```json
{
  "name": "string",
  "href": "string",
  "post_date": "YYYY-MM-DD",
  "views_count": 0
}
```
#### ❌ DELETE
`/api/videos/{id}/`  
Delete a video record by ID.

## 📄 API Documentation
This project is already using drf-yasg and drf-spectacular, access API docs via:
* Swagger UI: `http://127.0.0.1:8000/api/schema/swagger-ui/`

* Redoc UI: `http://127.0.0.1:8000/api/redoc/`


