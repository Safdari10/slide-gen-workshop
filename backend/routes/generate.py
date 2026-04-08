from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from io import BytesIO
from services.pptx_engine import build_presentation
from services.ai_generator import generate_slide_content
from agents.orchestrator import SlideOrchestrator

router = APIRouter()
orch = SlideOrchestrator()

class SlideRequest(BaseModel):
    prompt: str
    slide_count: int = 5
    theme: str = "default"

# @router.post("/generate")
# async def generate_slides(req: SlideRequest):
#     slides_data = generate_slide_content(
#         req.prompt, req.slide_count
#     )
#     pptx_bytes = build_presentation(slides_data)
#     return StreamingResponse(
#         BytesIO(pptx_bytes),
#         media_type=(
#             "application/vnd.openxmlformats-"
#             "officedocument.presentationml.presentation"
#         ),
#         headers={"Content-Disposition":
#             f"attachment; filename={req.prompt[:30]}.pptx"}
#     )

@router.post("/generate")
async def generate_slides(req: SlideRequest):
    slides_data = await orch.run(req.prompt, req.slide_count)
    pptx_bytes  = build_presentation(slides_data)
    return StreamingResponse(
        BytesIO(pptx_bytes),
        media_type=(
            "application/vnd.openxmlformats-"
            "officedocument.presentationml.presentation"
        ),
        headers={"Content-Disposition":
            f"attachment; filename={req.prompt[:30]}.pptx"}
    )