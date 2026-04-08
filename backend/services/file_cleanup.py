import shutil
from pathlib import Path

def cleanup_rendered_file(file_path: str) -> None:
    path = Path(file_path)
    media_root = path.parents[3]

    try:
        path.unlink(missing_ok=True)
    except OSError:
        return

    shutil.rmtree(media_root, ignore_errors=True)
