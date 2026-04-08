import json
from google.genai import types
from services.gemini_service import get_client, get_model_candidates


WRITER_PROMPT = """You are a slide content writer.
Given a title and focus, return ONLY valid JSON:
{"title":"...","bullets":["...","...","...","..."]}
Bullets: concise, punchy, audience-appropriate. JSON only."""


class WriterAgent:
    """Input: outline item {title, focus}
    Output: slide dict {title, bullets}"""

    async def run(self, item: dict) -> dict:
        client = get_client()
        errors: list[str] = []

        for model in get_model_candidates():
            try:
                resp = await client.aio.models.generate_content(
                    model=model,
                    contents=f"{WRITER_PROMPT}\n\n{json.dumps(item)}",
                    config=types.GenerateContentConfig(
                        max_output_tokens=400,
                        response_mime_type="application/json",
                    ),
                )
                raw = (resp.text or "").strip()
                if not raw:
                    raise RuntimeError("Writer returned an empty response")

                return json.loads(raw)
            except Exception as e:
                errors.append(f"[{model}] {type(e).__name__}: {e}")
                print(f"Writer [{model}] failed: {e}")

        return {
            "title": item.get("title", "Untitled"),
            "bullets": ["Content generation failed"],
        }
