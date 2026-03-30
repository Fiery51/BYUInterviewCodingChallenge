# BYU Interview Coding Challenge

Full-stack trivia app with:
- `trivia/frontend`: React + Vite
- `trivia/backend`: Flask API

## Project Structure

```text
BYUInterviewCodingChallenge/
  trivia/
    frontend/   # React client
    backend/    # Flask API
```

## Prerequisites

Install these first:
- Python 3.10+ (3.11 recommended)
- Node.js 18+ (Node 20 LTS recommended)
- npm (comes with Node.js)

Check versions:

```powershell
python --version
node --version
npm --version
```

## Setup and Run (Local Development)

Use two terminals: one for backend, one for frontend.

### 1) Backend (Flask)

From repo root:

```powershell
cd trivia\backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend starts at `http://localhost:5000`.

Health check:

```powershell
curl http://localhost:5000/api/health
```

### 2) Frontend (React + Vite)

Open a second terminal from repo root:

```powershell
cd trivia\frontend
npm install
npm run dev
```

Frontend starts at `http://localhost:5173`.

The frontend dev server proxies `/api/*` requests to `http://localhost:5000`.

## Everyday Commands

Frontend (`trivia/frontend`):
- `npm run dev` - Start dev server
- `npm run build` - Create production build
- `npm run preview` - Preview production build locally

Backend (`trivia/backend`):
- `python app.py` - Start Flask server

## Environment Variables (Optional)

Backend supports:
- `PORT` (default: `5000`)
- `FRONTEND_ORIGIN` (default: `http://localhost:5173`)

Example (PowerShell):

```powershell
$env:PORT=5001
$env:FRONTEND_ORIGIN="http://localhost:5173"
python app.py
```

## Troubleshooting

- `python` not found:
  - Install Python and ensure it is on your PATH.
- `node`/`npm` not found:
  - Install Node.js LTS and reopen terminal.
- `npm install` fails:
  - Delete `node_modules` and `package-lock.json`, then run `npm install` again.
- CORS or API errors in browser:
  - Ensure backend is running on port `5000`.
  - Ensure frontend is running on port `5173`.
- Port already in use:
  - Stop the process using that port, or change backend `PORT`.

## Notes

There is also a module-level README at `trivia/README.md` with a quick-start version of these steps.
