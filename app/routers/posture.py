from fastapi import APIRouter
from fastapi import status
from pydantic import BaseModel

from app.routers.camera import capture
from app.routers.model import PredictionResult
from app.routers.model import query_model
from app.utils.constanst import KIND_LEGS

router = APIRouter(prefix='/posture')


class PostureCheck(BaseModel):
    image: bytes
    prediction: PredictionResult
    kind: str


@router.get('/legs/check', response_model=PostureCheck, status_code=status.HTTP_202_ACCEPTED)
# captures photo and sends it to model to get prediction
async def check_legs():
    image = await capture()
    prediction = await query_model(image)

    return PostureCheck(image=image.data, prediction=prediction, kind=KIND_LEGS)
