# API Pengelolaan Aduan Sensitif

Sistem ini menangani aduan dengan deteksi konten sensitif otomatis menggunakan **FastAPI** dan **PostgreSQL**.

## 🚀 Fitur Utama

- CRUD data aduan
- Deteksi otomatis konten sensitif (rasisme, ujaran kebencian, pelecehan, kriminal)
- Admin dapat mengelola daftar kata/kalimat sensitif
- Penentuan status aduan berdasarkan tingkat sensitivitas
- Filter aduan berdasarkan status
- Sortir aduan berdasarkan waktu pembuatan atau sensitivitas
- Ekspor data aduan ke format **JSON** atau **CSV**

## 🛠️ Instalasi

### 1. Clone Repository
```bash
git clone https://github.com/PradanaB4CKUP/CodingTest_ImamAjiePradana.git
```

### 2. Buat Virtual Environment
```bash
python -m venv venv
```
Aktifkan virtual environment:
- **Windows:**
```bash
venv\Scripts\activate
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Setup Database
Pastikan PostgreSQL sudah berjalan dan buat database baru.

Edit atau buat file `.env` di root project:
```env
DATABASE_URL="postgresql://postgres:123123@localhost/aduan_db"
```

### 5. Jalankan Server
```bash
uvicorn app.main:app --reload
```

## 📄 Dokumentasi API
Akses dokumentasi otomatis di:
```
http://127.0.0.1:8000/docs
```

## 🔧 Struktur Project
```
app/
├── crud.py
├── database.py
├── main.py
├── models.py
├── schemas.py
├── routers/
│   ├── __init__.py
│   ├── aduan.py
│   └── sensitif.py
└── utils/
    ├── __init__.py
    └── deteksi.py
```

## 📊 Ekspor Data
Endpoint untuk ekspor aduan:
- Ekspor ke JSON:
```
GET /aduan/export?format=json
```
- Ekspor ke CSV:
```
GET /aduan/export?format=csv
```

## 🔧 Dependency
Daftar dependensi dalam `requirements.txt`:
```
fastapi
uvicorn
sqlalchemy
pydantic
psycopg2-binary
python-dotenv
pandas
```
## Error Database
jika masih terdapat error terutama error koneksi database
maka buatkan lerlebih dahulu database 'aduan_db' di postgresSql. kemudian jalankan kembali

