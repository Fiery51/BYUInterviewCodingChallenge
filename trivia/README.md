# Trivia App (React + Flask)

This repo is set up as a full-stack app:

- `frontend/`: React app (Vite)
- `backend/`: Flask API

## Quick Start

### 1) Backend

```powershell
cd trivia/backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend runs on `http://localhost:5000`.

### 2) Frontend

```powershell
cd trivia/frontend
npm install
npm run dev
```

Frontend runs on `http://localhost:5173`.
To view the program use any browser and go to http://localhost:5173 to view the website and play the trivia game!