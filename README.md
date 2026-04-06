# Quick start — clone, install, run

1. Clone

   git clone <repo-url>
   cd slide-gen-workshop

2. Backend (Python)

   cd backend

   # create venv and activate (Windows)

   python -m venv backend/.venv
   backend\.venv\Scripts\activate

   # or macOS / Linux

   python3 -m venv backend/.venv
   source backend/.venv/bin/activate

   pip install -r requirements.txt

   # run backend (development)

   uvicorn main:app --reload

3. Frontend (JS)

   cd frontend
   npm install
   npm run dev

4. Environment
   - Environment variables, copy or edit `backend/.env` before starting.
   - Backend defaults to port 8000; frontend (Vite) defaults to 5173.

That's it — open the frontend URL shown by Vite (usually http://localhost:5173) and verify the backend at http://localhost:8000/docs
