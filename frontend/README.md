# Frontend (React + TypeScript + Vite)

This frontend provides the UI for:

- Generating AI slide decks and downloading a `.pptx`
- Rendering and previewing a Manim video from the backend

## Prerequisites

- Node.js 20+
- npm
- Backend running on `http://127.0.0.1:8000` for local development

## Local development

```bash
cd frontend
npm install
npm run dev
```

The dev server starts at `http://localhost:5173`.

## API wiring (dev)

Vite proxy is configured in `vite.config.ts`:

- `/api/generate` -> `http://127.0.0.1:8000/generate`
- `/api/render` -> `http://127.0.0.1:8000/render`

This means frontend code always calls `/api/*` while Vite forwards to FastAPI.

## Build and preview

```bash
npm run build
npm run preview
```

## Docker behavior

In Docker, the app is served by Nginx on port `80` (mapped to `3000` in `docker-compose.yml`).

- Public URL: `http://localhost:3000`
- API proxy uses `BACKEND_ORIGIN` (default: `http://backend:8000`)

## Main frontend flow

- `src/hooks/useSlideGenerator.ts` posts slide requests and triggers file download
- `src/hooks/useManim.ts` posts render requests and creates a browser video URL

## Useful scripts

- `npm run dev` - start Vite dev server
- `npm run build` - production build
- `npm run preview` - preview production build locally
- `npm run lint` - run lint checks
