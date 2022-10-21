from fastapi import APIRouter
from pydantic import BaseModel

from app.routers import Health
from app.routers.camera import Image

router = APIRouter(prefix='/model')


class PredictionResult(BaseModel):
    prediction: bool
    confidence: float


@router.get('/', response_model=Health)
async def health():
    return Health(status='ok')


@router.post('/legs/predict', response_model=PredictionResult)
# implements http rest api call to tensorflow model responsible for establishing whether posture is ok or not
async def query_model(data: Image):
    # image = data.data

    try:
        return PredictionResult(prediction=True, confidence=1)
    except Exception:
        return PredictionResult(prediction=False, confidence=1)
