# Slide Gen Workshop

A full-stack workshop app that generates downloadable PowerPoint slides with AI and can render a sample Manim scene.

## Tech stack

- Backend: FastAPI, Pydantic, python-pptx, Google GenAI, Manim
- Frontend: React + TypeScript + Vite
- Containerized run: Docker + docker-compose

## Project layout

```text
slide-gen-workshop/
	backend/     # FastAPI API for slide generation and rendering
	frontend/    # React UI (Vite in dev, Nginx in Docker)
```

## Run locally

### 1) Backend

```bash
cd backend
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies and run:

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Create `backend/.env` with:

```env
GOOGLE_API_KEY=your_key
GOOGLE_MODEL=gemini-2.5-flash
FALLBACK_MODEL=gemini-1.5-flash
```

### 2) Frontend

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Vite runs on `http://localhost:5173` and proxies `/api/*` to `http://127.0.0.1:8000`.

## Run with Docker

From the repository root:

```bash
docker compose up --build
```

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`

`docker-compose.yml` loads environment variables from `backend/.env`.

## API endpoints

- `GET /health` - health check
- `POST /generate` - returns a generated `.pptx` file
- `POST /render?scene_class=TitleSlide` - returns a rendered `.mp4`

Interactive API docs: `http://localhost:8000/docs`

## Notes

- The frontend downloads generated `.pptx` files directly in the browser.
- The backend currently renders `manim_scenes/title_scene.py` for `/render`.
- For component-level details, see `backend/README.md` and `frontend/README.md`.
