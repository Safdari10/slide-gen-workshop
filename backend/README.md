# Backend (FastAPI)

This backend exposes endpoints to:

- Generate AI slide content and return a downloadable PowerPoint (`.pptx`)
- Render a Manim scene and return a video (`.mp4`)

## Prerequisites

- Python 3.11+
- Virtual environment (recommended)
- System dependencies required by Manim (already handled in Docker)

## Setup (local)

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

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `backend/.env`:

```env
GOOGLE_API_KEY=your_key
GOOGLE_MODEL=gemini-2.5-flash
FALLBACK_MODEL=gemini-1.5-flash
```

Run development server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open docs at `http://localhost:8000/docs`.

## Endpoints

- `GET /health`
  - Returns: `{ "status": "ok" }`

- `POST /generate`
  - Body:
    ```json
    {
      "prompt": "Intro to machine learning",
      "slide_count": 5,
      "theme": "default"
    }
    ```
  - Response: PowerPoint file stream (`application/vnd.openxmlformats-officedocument.presentationml.presentation`)

- `POST /render?scene_class=TitleSlide`
  - Query param: `scene_class` (defaults to `TitleSlide`)
  - Response: MP4 video stream

## Internal structure

- `main.py` sets up FastAPI, CORS, and route registration
- `routes/generate.py` orchestrates AI generation + PPTX building
- `routes/render.py` runs Manim rendering and returns a video file
- `services/ai_generator.py` calls Google GenAI and parses JSON output
- `services/pptx_engine.py` creates the final `.pptx`

## Docker

The backend Docker image:

- Installs Python dependencies from `requirements.txt`
- Installs native packages needed by Manim rendering
- Exposes port `8000`
