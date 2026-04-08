from fastapi import APIRouter
from fastapi.responses import FileResponse
from starlette.background import BackgroundTask
from services.manin_render import render_manim_scene
from services.file_cleanup import cleanup_rendered_file

router = APIRouter()


@router.post("/render")
async def render_slide(scene_class: str = "TitleSlide"):
    path = render_manim_scene(
        "manim_scenes/title_scene.py",
        scene_class,
        quality="l"
    )
    return FileResponse(
        path,
        media_type="video/mp4",
        background=BackgroundTask(cleanup_rendered_file, path),
    )
