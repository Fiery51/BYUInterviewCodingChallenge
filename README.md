# BYU Interview Coding Challenge
This project is a full-stack trivia game built with React and Flask.  
Users can start a game, answer a series of trivia questions fetched from the Open Trivia DB API, and receive a final score based on their performance.

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


## Assumptions / Notes
- This game uses the Open Trivia DB to fetch 10 random questions at the start of a game and are stored in memory
- Currently I just prioritize game flow over anything else, leaving polish out to ensure that the website and game works


## Tools and Libraries Used
- React + Vite for the frontend
- Flask for the backend
- JavaScript and Python

## Additions if I had more time
- Allowing the user to pick categories
- Additional styling
- User login and Database storage to allow data persistence
- mobile styling
- Backend tests to switch to test driven development
- refactoring the backend to optimize code