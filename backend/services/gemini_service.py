from google import genai
from config import FALLBACK_MODEL, GOOGLE_API_KEY, MODEL


_client = None   


def get_client() -> genai.Client:
	"""Create a configured Gemini client instance."""
	if not GOOGLE_API_KEY:
		raise RuntimeError("GOOGLE_API_KEY is not set")
	global _client
	if _client is None:
		_client = genai.Client(api_key=GOOGLE_API_KEY)

	return _client


async def close_client() -> None:
	"""Close Gemini client connections (if any)."""
	global _client
	if _client is not None:
		if hasattr(_client, "aclose"):
			await _client.aclose()
		elif hasattr(_client, "close"):
			_client.close()
		_client = None


def get_model_candidates() -> list[str]:
	"""Return deduplicated model candidates in fallback order."""
	candidates: list[str] = []
	for name in [MODEL, FALLBACK_MODEL]:
		model_name = (name or "").strip()
		if model_name and model_name not in candidates:
			candidates.append(model_name)
	return candidates

