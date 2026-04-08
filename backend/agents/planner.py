import json
from google.genai import types

from services.gemini_service import get_client, get_model_candidates

PLANNER_PROMPT = """You are a presentation architect.
Given a topic and slide count, return ONLY valid JSON:
{"outline": [{"slide_number":1,"title":"...","focus":"one sentence"}]}
No markdown. JSON only."""


class PlannerAgent:
    """Input:  prompt (str), slide_count (int)
    Output: outline list[{slide_number, title, focus}]"""

    async def run(self, prompt: str, slide_count: int) -> list[dict]:
        client = get_client()
        errors: list[str] = []

        for model in get_model_candidates():
            try:
                resp = await client.aio.models.generate_content(
                    model=model,
                    contents=f"{PLANNER_PROMPT}\n\nTopic: {prompt}. Slides: {slide_count}",
                    config=types.GenerateContentConfig(
                        max_output_tokens=800,
                        response_mime_type="application/json",
                    ),
                )
                raw = (resp.text or "").strip()
                if not raw:
                    raise RuntimeError("Planner returned an empty response")
                return json.loads(raw)["outline"]
            except Exception as e:
                errors.append(f"[{model}] {type(e).__name__}: {e}")

        raise RuntimeError("All models failed: " + " | ".join(errors))
