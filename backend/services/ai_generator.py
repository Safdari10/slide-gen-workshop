import json
from google.genai import types
from services.gemini_service import get_client, get_model_candidates


SYSTEM_PROMPT = """You are a professional presentation writer.
Given a topic and slide count, return ONLY valid JSON - no markdown:
{"slides": [{"title": "...", "bullets": ["...", "...", "..."]}]}"""


def _extract_json_payload(raw_text: str) -> dict:
    """Parse Gemini output even when wrapped in markdown code fences."""
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:].strip()
    return json.loads(text)


def generate_slide_content(prompt: str, slide_count: int = 5) -> list[dict]:
    client = get_client()
    errors: list[str] = []

    for model_name in get_model_candidates():
        try:
            resp = client.models.generate_content(
                model=model_name,
                contents=f"{SYSTEM_PROMPT}\n\nTopic: {prompt}. Slides: {slide_count}",
                config=types.GenerateContentConfig(
                    max_output_tokens=1500,
                    temperature=0.7,
                    response_mime_type="application/json",
                ),
            )
            if not getattr(resp, "text", None):
                raise RuntimeError("Gemini returned an empty response")

            parsed = _extract_json_payload(resp.text)
            slides = parsed.get("slides")
            if not isinstance(slides, list):
                raise RuntimeError("Response JSON missing 'slides' list")

            return slides
        except Exception as e:
            errors.append(f"[{model_name}] {type(e).__name__}: {e}")

    raise RuntimeError("All models failed: " + " | ".join(errors))
