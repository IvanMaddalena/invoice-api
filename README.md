# 💼 Invoice API

**A production-ready backend API to manage users and invoices.**  
Built with **FastAPI**, powered by **PostgreSQL**, and containerized with **Docker**.

---

## 🚀 Why this project?

This project simulates a real-world invoice management system, designed to demonstrate:

- Clean backend architecture with FastAPI
- SQL database integration (PostgreSQL/SQLite)
- API-first development approach (OpenAPI docs ready)
- Dockerized and CI-ready backend

> Ideal for portfolio, remote job applications, and backend tech interviews.

---

## 🧠 Key Features

- ✅ Create and manage **users**
- ✅ Create and track **invoices**
- ✅ Mark invoices as **paid/unpaid**
- ✅ Filter invoices by user
- ✅ Full RESTful API with clear models
- ✅ Ready for testing, Docker, and future extensions (auth, PDF, email)

---

## 🛠️ Tech Stack

| Layer       | Tech                                   |
|-------------|----------------------------------------|
| Framework   | FastAPI                                |
| ORM         | SQLAlchemy                             |
| Database    | SQLite (default) or PostgreSQL via Docker |
| Container   | Docker + Docker Compose                |
| Testing     | Pytest + HTTPX                         |
| Docs        | Auto-generated at `/docs`              |

---

## 📦 Project Structure

```plaintext
invoice-api/
├── app/                  # Source code
│   ├── main.py           # App entrypoint
│   ├── database.py       # DB connection
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic validation
│   ├── crud.py           # DB operations
│   └── routes.py         # API endpoints
├── tests/                # Test files
├── requirements.txt      # Dependencies
├── .gitignore            # Exclusions
├── Dockerfile            # Image definition
├── docker-compose.yml    # API + DB setup
└── README.md
```

---

## 📂 Example API Endpoints

| Endpoint               | Method | Description                |
|------------------------|--------|----------------------------|
| `/users/`              | POST   | Create a new user          |
| `/users/`              | GET    | Get all users              |
| `/invoices/`           | POST   | Create a new invoice       |
| `/invoices/`           | GET    | List all invoices          |

All endpoints return JSON. Explore full interactive docs at:
```
http://localhost:8000/docs
```

---

## ⚙️ How to Run

### ▶️ Locally (SQLite)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start API
uvicorn app.main:app --reload
```

---

### 🐳 With Docker + PostgreSQL

```bash
# Build and run API and database
docker-compose up --build
```

This will expose:
- API at `http://localhost:8000`
- PostgreSQL at `localhost:5432` (user: `user`, password: `password`)

---

## 🧪 Testing (optional)

Run basic unit tests using:
```bash
pytest
```

> Add new tests inside the `tests/` folder.

---

## 🏗️ Future Improvements

- [ ] Add JWT authentication
- [ ] Filter invoices by status/date
- [ ] Export invoices to PDF
- [ ] Email invoice confirmations
- [ ] Admin dashboard (React or Streamlit)

---

## 👤 Author

**Ivan Maddalena**  
📍 Based in Italy — open to remote worldwide  
📫 [ivan.maddalena00@gmail.com](mailto:ivan.maddalena00@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/ivanmaddalena)  
🌍 [GitHub](https://github.com/IvanMaddalena)

---

## 🪪 License

MIT License – free to use, fork, and build upon.
