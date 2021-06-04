from tempfile import NamedTemporaryFile

from fastapi import APIRouter
from starlette.responses import FileResponse

from src.drawing import draw
from src.models import Drawing

router = APIRouter()


@router.post("/drawings")
def drawings(drawing: Drawing):
    with NamedTemporaryFile(mode="w+b", suffix=".png", delete=False) as file:
        draw(drawing).savefig(file, format="png")
        return FileResponse(file.name, media_type="image/png")
