# Quick Start — Clone, Install, Run

## 1. Clone

```bash
git clone <repo-url>
cd slide-gen-workshop
```

## 2. Backend (Python)

```bash
cd backend
```

Update the `.env` file with the required values before starting.

### Create virtual environment and activate (Windows)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Or macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run backend (development)

```bash
uvicorn main:app --reload
```

## 3. Frontend (JavaScript)

Open a new terminal:

```bash
cd frontend
npm install
npm run dev
```

## 4. Environment

- Backend default: `http://localhost:8000`
- Frontend (Vite) default: `http://localhost:5173`

## 5. Verify the app

Open the frontend URL shown by Vite (usually `http://localhost:5173`).

Verify the backend API docs at:

```text
http://localhost:8000/docs
```
