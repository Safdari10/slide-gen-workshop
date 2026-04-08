from fastapi import APIRouter
from fastapi.responses import FileResponse
from backend.manim_scenes.title_scene import TitleScene

router = APIRouter()

@router.get("/render")
def render_title_scene(scene_class: str = "TitleSlide"):
    path = render_manim_scene("backend/manim_scenes/title_scene.py", scene_class)
    return FileResponse(path, media_type="video/mp4", filename=f"{scene_class}.mp4")